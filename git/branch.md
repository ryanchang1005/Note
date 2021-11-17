# branch
- 新增branch並checkout過去
```
git checkout -b new-branch
```
- 修改當前branch名稱
```
git branch -m new-name-branch
```
- 刪除branch
```
git branch -d new-branch
```
- 顯示所有branch資訊
```
git branch -a
------------------------
master
issue/123
remotes/origin/master
remotes/origin/issue/123
```
- 刪除remote branch
```
git push origin :issue/123
```
- 顯示remote branch資訊
```
git remote show origin
```
- 刪除remote過時的branch
```
git remote prune origin
```