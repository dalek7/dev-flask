# Flask test 기록
Flask http server on the docker in the remote server

```
Docker --> server --> client
81 --> 7981 --> 7981
```
## Get
* Docker run
    * 아래 -v 옵션에서의 폴더는 각자 환경에 
```bash
docker run -u $(id -u) -it --rm --gpus all -v ~/repos/:/tf/repos/ -p 7981:81 DOCKER_IMAGE bash
```

*  Server-->Local SSH-port forwarding
```bash
ssh -N -f -L localhost:7981:localhost:7981 ID_SERVER@IP_SERVER -p SERVER_SSH_PORT
```

### hello_getparams.py
인자 받아보기

<img src='images/img01.png' />


### hello_getparams2.py
인자 받아서 처리

<img src='images/img02.png' />

## Post 
### hello_post1.py
Post 보내고 처리하는 예시

https://github.com/dalek7/dev-flask/blob/fc7d2929319e735b7995dd856820844da6be658c/hello_post1.py#L24-L31

Browser 에서
```
http://localhost:7981/send_post
```


```
key: param1, value: test
key: param2, value: 123
key: param3, value: 한글
```
