# grep

```bash
# 找出檔案名稱中含有".txt"的檔案
$ ls | grep .txt

# 顏色標示
$ grep --color=always -n 123 *.txt

# a開頭
grep "^a" data.txt

# b結尾
grep "b$" data.txt
```
