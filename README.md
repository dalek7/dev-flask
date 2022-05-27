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
### hello_post2_data.py
Browser 에서
```
http://localhost:7981/send_post2
```

실행 예시
```
key: n_layers, value: 8
key: dt_load, value: 2.319
key: dt_pred, value: 0.034
key: x_idx, value: 6580
key: xshape, value: [1, 100, 6]
key: y, value: [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
key: y_pred, value: [1.1816934602393303e-05, 5.228307742299876e-08, 0.009548296220600605, 3.074364764502069e-13, 0.9841724634170532, 6.795051376684569e-06, 4.346143236966249e-11, 1.319934023191749e-10, 2.769366744814761e-07, 2.9031187409600534e-07, 1.904954274323245e-07, 5.822041460046279e-11, 0.0048309266567230225, 1.4514494068862405e-05, 0.0014121300773695111, 6.255621021189484e-10, 1.2721361464240744e-10, 2.182621756219305e-06]
key: y_argmax, value: 4
key: y_pred_argmax, value: 4
key: y_pred_proba, value: 0.984
```

```
key: n_layers, value: 8
key: dt_load, value: 2.319
key: dt_pred, value: 0.034
key: x_idx, value: 10760
key: xshape, value: [1, 100, 6]
key: y, value: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
key: y_pred, value: [0.067682184278965, 9.290540958772908e-08, 9.844524624177348e-19, 6.562713110724872e-07, 2.2790984052258045e-13, 0.02254042588174343, 1.6706307448544067e-08, 0.9097420573234558, 1.2408015209075529e-05, 4.157478828272665e-18, 4.808447429680206e-19, 5.22789740896979e-16, 1.0730669686154215e-08, 6.79550726800926e-09, 2.217981636931654e-05, 3.585749475121247e-10, 8.296413001041003e-10, 8.738646829974745e-20]
key: y_argmax, value: 7
key: y_pred_argmax, value: 7
key: y_pred_proba, value: 0.910
```
