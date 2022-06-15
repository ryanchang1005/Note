# base64

```bash
# encode
$ echo "abc.com" | base64  # YWJjLmNvbQo=

# decode
$ echo "YWJjLmNvbQ==" | base64 -d  # abc.com
```