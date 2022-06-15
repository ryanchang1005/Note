# Replica Set 高可用建置
Replication(複寫, 副本)是在多個或跨多個server上同步資料的過程
官方 : Replication is the process of synchronizing data across multiple servers.

## 官方提供的三種Replica Set架構
* Three Member Replica Sets
* Replica Sets with Four or More Members
* Geographically Distributed Replica Sets

## Three Member Replica Sets
最常見由三個MongoDB節點組成
寫到Primary時資料會自動複製到2個Secondary
2個Secondary則是透過Heartbeat確認對方還沒掛掉
```
                        [Secondary]
                        /(Replication)
Read/Write <> [Primary]       |  (Heartbeat)
                        \(Replication)
                        [Secondary]
```
如果Primary掛掉時Secondary之間會選出一台Primary

## Replica Sets with Four or More Members
由更多的節點組成, 備援更強

## Geographically Distributed Replica Sets
分散式, 異地備援

---

# Sharding(分片)
有兩種range based partitioning 或 hash based partitioning

## range based partitioning
例如 : 0~10到A, 11~20到B, 21~30到C

## hash based partitioning
例如 : 
hash(key) = 1 >> Shard1
hash(key) = 2 >> Shard2
hash(key) = 3 >> Shard3
```
               - ShardA > Replica Set
Router(mongos) - ShardB > Replica Set
               - ShardC > Replica Set

```