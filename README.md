# docker

Simple Docker examples for learning.

## hello-world
Basic Python container that prints "Hello, World!"

```bash
cd hello-world
docker build -t hello-world .  # -t tags/names the image
docker run hello-world
```

## http-request
Python container that makes an HTTP request using the requests library.

```bash
cd http-request
docker build -t http-request .  
docker run http-request
``` 
