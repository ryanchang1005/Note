# submodule

- 建立 submodule
```
git submodule add https://github.com/example/xxx_proto proto
```

- 刪除 submodule
```
git rm <path-of-submodule>
```

- 將所有 submodule repo 都抓下來
```
git submodule init
git submodule update --init --recursive
```