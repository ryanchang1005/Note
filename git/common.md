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

# Diff
- 顯示與上次commit此檔案的異動內容
```
git diff <filename>
```