# Command line

- 登入
```
mysql -h hostname -u root -p database_name
```

- 備份
```
mysqldump -h hostname -u root -p database_name > database_name_backup.sql
```

- 復原
```
mysql -h hostname -u root -p database_name < database_name_backup.sql
```