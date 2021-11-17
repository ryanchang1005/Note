# Submodule
- clone時一並把submodule的repo也clone下來
```
git clone --recursive https://github.com/ryanchang1005/Note.git
```
- 事後才知道有submodule想把submodule裡的repo也clone下來
```
git submodule init
git submodule update --recursive
```

# Remote
- 顯示remote url
```
git remote -v
```
- 修改remote url
```
git remote set-url origin https://github.com/ryanchang1005/Note.git
```

# Branch
- 新增branch並checkout過去
```
git checkout -b new-branch
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

# Reset
- 捨棄該檔案尚未commit的內容, 多改的就捨棄了
```
git checkout -- ooo.txt
```
- 捨棄此次的所有修改, 直接回到上一次的commit(危)
```
git reset --hard
```
- git add 後反悔, 退回unstage區
```
git reset <filename>
```

# Diff
- 顯示與上次commit此檔案的異動內容
```
git diff <filename>
```