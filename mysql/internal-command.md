# Internal command

- 顯示所有資料庫
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

- 建立資料庫
```
mysql> create database my;
Query OK, 1 row affected (0.01 sec)
```

- 使用資料庫
```
mysql> use my;
Database changed
```

- 顯示 table
```
mysql> show tables;
Empty set (0.01 sec)
```

- 顯示所有 procedure
```SQL
SELECT name FROM mysql.proc 
```

- 顯示所有資料庫容量
```SQL
SELECT 
    table_schema AS "Database", 
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS "Size (MB)" 
FROM information_schema.TABLES 
GROUP BY table_schema;
```

- 顯示指定資料庫table容量
```SQL
SELECT 
    table_name AS "Table",
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)"
FROM information_schema.TABLES
WHERE table_schema = "my"
ORDER BY (data_length + index_length) DESC;
```

- 加 index
```SQL
CREATE INDEX `idx_user_id` on `event`(`user_id`) USING BTREE;
CREATE INDEX `idx_create_at` on `event`(`create_at`) USING BTREE;
```

- 刪除 index
```SQL
DROP INDEX `index_name` ON `table_name`;
```

- 顯示 table 的 index
```SQL
SHOW INDEX FROM `table_name` FROM `database_name`;
```