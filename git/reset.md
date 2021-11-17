# reset
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