# openssl

```bash
# generate rsa key
openssl genrsa -out pri.pem 2048
openssl rsa -in pri.pem -out pub.pem -outform PEM -pubout
openssl rsa -in pri.pem -pubout -outform DER | openssl sha1 -c

# generate tls key pair
$ openssl req -x509 -sha256 -nodes -days 3650 -newkey rsa:2048 -keyout server.key -out server.crt

# compute HMAC
$ echo -n "password" | openssl sha256 -hmac "123"
```