# Command line

- 登入
```
mysql -h hostname -u root -p database_name
```

- 匯出
```
mysqldump -h hostname -u root -p database_name > database_name_backup.sql
```

- 匯入
```
mysql -h hostname -u root -p database_name < database_name_backup.sql
```