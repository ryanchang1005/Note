## Common
```
KEYS *name*  // 列出符合後方表達式的Key
TYPE <key>  // 列出Key的類型
EXPIRE <key> <timeout>  // 設定Key的過期時間(秒)
TTL <key>  // 取得Key的過期時間
FLUSHALL  // 清除所有Key(危)
DEBUG OBJECT <key>  // 列出Key詳細資訊, serializedlength(Byte)
```

## Data structure
```
key :  "I am a string."                      String
key :  001101001001001001001                 Bitmap
key :  {12345}{128749812740}{889787231}      Bit field
key :  {name: "ryan", age: "25"}             Hash
key :  ["A", "A", "A", "D"]                  List
key :  {"A", "B", "C", "D"}                  Set
key :  {"A": 1, "B": 3, "C": 100, "D": 1299} Sorted Set
key :  {"A": (121, 35), B: (200, 100)}       Geospatial Indexes
key :  00101111 00011101 01100011            Hyperloglog
```

## Key
```
最好都用一種模式, "object-type:id:field", 遇到多單字用點隔開
"user:1000:session"
"post:12345:comment.count"
```

## String
```
SET <key> <value>
GET <key>
GETSET <key> <value>  // 拿舊值, 設新值
SETEX <key> <timeout> <value>  // 設值並給予過期時間
SETNX <key> <value>  // 如此Key不存在, 則設值
INCR <key>  // Key的值 加1
DECR <key>  // Key的值 減1

除了string以外還可以存int, 也可存圖片, 最大512MB
使用情境 : 常用key-value cache應用, 文章留言數, 追隨者數量
```

## Hash
```
HMSET user.1 name "ryan" age "25"  // 設定key="user.1", value="{"name": "ryan", "age": "25"}"
HGETALL user.1  // 取出所有資料(key, value)
HKEYS user.1  // 只取出key
HVALS user.1  // 只取出value
HLEN user.1  // key-value對的數量
HMGET user.1 "name"  // 取出指定key的值
HMSET user.1 "name" "ryan2"  // 設定指定key的值
```

## Set
```
SADD <key> <member> // 加 / O(1)
SREM <key> <member> // 移除 / O(1)
SCARD <key> // 數量 / O(1)
SISMEMBER <key> <member> // member是否存在 / O(1)
SMEMBERS <key> // 顯示set有哪些member / O(N)
```

## List
```
LPUSH <key> <v1> <v2> <v3>  // 從左側推資料進去  ["v1", "v2", "v3"]
LRANGE <key> <from_index> <to_index>  // 取得指定範圍資料
RPOP <key>  // 取得並彈出右邊第一個值
BRPOP <key> <timeout> // 如list為空則阻塞等待, 如有資料取得並彈出右邊第一個值, 無資料則阻塞直到過期

使用場景:消息對列
```

## SortedSet
```
ZADD <key> <score1> <member1>  // 增加
ZRANGE <key> 0 10 WITHSCORES  // 根據score由小到大前10筆, 並帶著score
ZINCRBY <key> <increment> <member>
ZCOUNT <key> <min> <max>  // 數score介於min和max的數量, ZCOUNT <key> -inf +inf 數全部
ZREM <key> <member> // 刪除member

基本上與Set相同, 但每個member都會帶著一個score, 並且根據score遞增排序

使用情境:排行榜
```

## Hyperloglog
```
PFADD <key> <value>  // 
PFCOUNT <key>  // 
PFMERGE <new_key> <key1> <key2> // 合併key

基本上和Set相同, 但使用空間更少, 只能用PFCOUNT回傳不重複個數, 多用於統計UV資料
127.0.0.1:6379> pfadd user:login:2020-01-01T00 a b c  // a, b, c 在0時登入
(integer) 1
127.0.0.1:6379> pfcount user:login:2020-01-01T00  // 統計在0時登入人數(不重複)
(integer) 3
127.0.0.1:6379> pfadd user:login:2020-01-01T01 a b c d  // a, b, c, d 在1時登入
(integer) 1
127.0.0.1:6379> pfcount user:login:2020-01-01T01  // 統計在1時登入人數(不重複)
(integer) 4

// 為了計算出0~1時不重複登入人數, 使用pfmerge建出user:login:2020-01-01T00-01
127.0.0.1:6379> pfmerge user:login:2020-01-01T00-01 user:login:2020-01-01T00 user:login:2020-01-01T01
OK
127.0.0.1:6379> pfcount user:login:2020-01-01T00-01
(integer) 4

```

## GEO
```
新增
GEOADD key longitude latitude member [longitude latitude member ...]
GEOADD places 121.5173748 25.0477022 "taipei main station" 121.5645294 25.0338489 "taipei 101"

查詢
GEOPOS places "taipei main station" "nothing" "taipei 101"
1) 1) "121.51737481355667114"
   2) "25.04770260439912732"
2) (nil)
3) 1) "121.56452804803848267"
   2) "25.03384781854217778"

算距離
GEODIST places "taipei main station" "nothing"
(nil)
GEODIST places "taipei main station" "taipei 101"
"4995.3511"
GEODIST places "taipei main station" "taipei 101" km
"4.9954"

以"給予的點"或"成員"為圓心, 周遭距離N公里的成員, 距離(m, km), 可以帶著"與中心距離", "成員的經緯度", "限制數量", "依照距離遞增或遞減"
GEORADIUS places 121.5217817 25.0346137 5 km WITHDIST WITHCOORD COUNT 10 ASC
以中正紀年堂為中心(121.5217817 25.0346137), 周遭5公里的成員, 依照距離遞增, 前10筆

與上方相同只是不是用"給予的點", 而是用"成員"(含自己)
GEORADIUSBYMEMBER places "taipei 101" 5 km WITHDIST WITHCOORD COUNT 10 ASC

取出, 並用geohash值顯示
GEOHASH places "taipei main station" "taipei 101"
1) "wsqqmpy32n0"
2) "wsqqqm28dz0"

geohash值(https://ithelp.ithome.com.tw/articles/10203720)

```

## 大量key同時失效
```
有時候我們會大量設置cache並給予相同的timeout時間, 或是定時任務每天, 小時設置首頁cache
一但timeout時一到所有cache瞬間失效, 會使得client端瞬間大量往資料庫去做查詢
輕則會導致頁面卡頓, 回應延遲, 重則資料庫服務連線爆掉, 甚至崩潰
可以隨機值設置timeout時間降低同時cache失效問題
```

## 分佈式鎖
```
使用SETNX <key> <value>
要取鎖的時候執行SETNX
如返回1則取鎖成功, 使用完畢需調用DEL <key>將鎖釋放
如返回0則取鎖失敗, 可選擇阻擋, 迴圈重試直到某種timeout釋放鎖
"""通常需搭配timeout機制否則鎖無法釋放"""
```

## 消息隊列(MessageQueue)
```
可以使用List來實現生產者與消費者模式
例如使用LPUSH和RPOP來實現
但當list是空的卻一直撈取資料(RPOP)會浪費資源而且每次撈取皆為空值
而Redis有提供BRPOP, BLPOP提供阻塞式的指令
而且消費者還可以指定阻塞時等待的時間, 時間內得到資料則返回, 超時還沒有資料則返回0
```

## 持久化(Persistence)
```
```

## 主從同步, 複寫(Replication)
```
```

## 哨兵(Sentinel) & 叢集(Cluster)
```
```