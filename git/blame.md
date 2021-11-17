# blame
- 顯示該檔案每一行異動的作者, 時間, commit
```
git blame <filename>
git blame -L 10,20 <filename>          // 顯示10到20行的
git blame -L 50,+20 <filename>         // 從50行開始再顯示20行(50-70)
git blame <filename> | grep <username> // 找出特定user的傑作:)
```
- 通常搭配log找出該行commit的內容
```
git log -p <commit>
```