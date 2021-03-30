# Schema的設計1

## 大概分成三種設計規則
* One-to-Few
* One-to-Many
* One-to-Squillions

## 注意
```
需注意Document Size不可超過16MB
把關聯的資料直接放在物件中的動作叫Embedding(嵌入)
```

## One-to-Few
一個物件關聯少量的物件(通常是1000以內)
資料量不大, 可以一次查出東西來, 最基本的反正規劃技巧
例如 : 人與地址的關係
```JSON
db.person.findOne()
{
    "id": 1,
    "name": "ryan",
    "addresses": [
        {"address": "AAABBBCCC", lat: "25", lng: "121"},
        {"address": "AAADDDEEE", lat: "25", lng: "122"}
    ]
}
```

## One-to-Many
一個物件關聯有點多量的物件(幾千幾百個這種等級)
例如 : 某地區的便利商店數
```JSON
db.citys.findOne()
{
    "_id": OjbectID("A1"),
    "name": "NewTaipei",
    "shops": [
        OjbectID("ABC001"),
        OjbectID("ABC002"),
        OjbectID("ABC003")
    ]
}
db.shops.findOne()
{
    "_id": OjbectID("ABC001"),
    "name": "7-11",
    "open_time": "09:00 ~ 21:00"
}

在應用層Join起來
city = db.citys.findOne({"_id": OjbectID("A1")})
shops = db.shops.find({"_id": { $in: city.shops}}).toArray()

因為存在兩個地方, 當要刪除shop時另一邊的city也要刪除確保一致性
```

## One-to-Squillions
一個物件關聯海量的物件(千,萬級以上)
```JSON
db.servers.findOne()
{
    "_id": OjbectID("server-001"),
    "ip": "123.123.123.123"
}
db.logs.findOne()
{
    "_id": OjbectID("481923"),
    "message": "test",
    "time": "2021-03-01T00:00:00Z",
    "server": OjbectID("server-001"),
}

在應用層查詢出來
server = db.servers.findOne({"ip": "123.123.123.123"})
logs = db.logs.find({"server": server._id}).sort({"time": -1}).limit(300).toArray()
```

### So
怎麼選擇哪種模式則是根據物件關聯的數量做選擇

---

# Schema的設計2
利用Two-Way Referencing(雙向參考)與Denormalization(反正規化)來讓查詢更有效率

## Two-Way Referencing
```JSON
聊天室與訊息的關係
db.chats.findOne()
{
    "_id": ObjectID("A01"),
    "name": "My sport chat",
    "chat_type": "group",
    "messages": [
        ObjectID("MSG-01"),
        ObjectID("MSG-02"),
        ObjectID("MSG-03"),
    ]
}
db.messages.findOne()
{
    "_id": ObjectID("MSG-01"),
    "who": "ryan":
    "message": "Hi",
    "time": "2021-03-01T00:00:00Z",
    "chat": ObjectID("A01"),
}
好處是不管你從chat找message或message找chat都很方便
缺點是刪除或異動要兩邊都刪, 必須手動處理同步問題
```

## Denormalizing Many > One
```JSON
db.citys.findOne()
{
    "_id": OjbectID("A1"),
    "name": "NewTaipei",
    "shops": [
        OjbectID("ABC001"),
        OjbectID("ABC002"),
        OjbectID("ABC003")
    ]
}
db.shops.findOne()
{
    "_id": OjbectID("ABC001"),
    "name": "7-11",
    "open_time": "09:00 ~ 21:00"
}
假設以上面城市和店家的例子, 我們很常從城市去找店家名稱好了
我們可以把city的結構改成
db.citys.findOne()
{
    "_id": OjbectID("A1"),
    "name": "NewTaipei",
    "shops": [
        {"_id": OjbectID("ABC001"), "name": "7-11"},
        {"_id": OjbectID("ABC002"), "name": "全家"},
        {"_id": OjbectID("ABC003"), "name": "全聯"},
    ]
}
應用層做JOIN
city = db.citys.findOne({"_id": OjbectID("A1")})
shop_ids = city.shops.map(function(obj){return obj._id})
db.shops.find({"_id": { $in : shop_ids }}).toArray()

優點就是這樣就可以少去一層join, 就可以大大提升效率
缺點是name存了兩個地方, 要異動時需保持同步一致性

自我碎碎念 : 其實city的shops就有點像cache, 在異動的時候可以以同步的方式去異動city.shop的值, 再用非同步(MQ)去異動原始shop的值即可, 但就是會多一些非同步更新時失敗的處理機制
```

## Denormalizing Many > One
```JSON
相反的如果想要用商店去反向查到城市的其他資訊, 可將shop改為下
db.shops.findOne()
{
    "_id": OjbectID("ABC001"),
    "name": "7-11",
    "open_time": "09:00 ~ 21:00",
    "city_name": "NewTaipei"  # 從city反正規化來的
}
```

## So
* 反正規化後就會失去資料的一致性
* 所以在讀取頻率高, 寫頻率低的情況反正規化比較有意義
