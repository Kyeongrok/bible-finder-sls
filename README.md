# Serverless로 만든 API Server

## Serverless Framework설치

- npm있으면 설치 할 수 있습니다.

```
npm install -g serverless
```

위 명령어로 serverless framework을 먼저 설치 해주세요.

## 권한 설정

aws configure를 이용해 access key와 secret을 넣어주세요.

```
aws configure
```

![image](https://user-images.githubusercontent.com/1642243/147857376-84b43ad6-4082-4ad7-bc8b-81a8e4bb05ec.png)


## sls 배포
* sls deploy --stage dev
* sls deploy function -f findBetween --stage dev

### 배포 후 test
* sls invoke -f hello --log

### local test
* sls invoke local -f hello --log


### 데이터 넘기기
* sls invoke -f call-telegram --log -d '{"a":"bar"}'

### 로그 보기
* sls logs -f hello

## request요청
* https://2kstde4150.execute-api.ap-northeast-1.amazonaws.com/dev/v1/find/single/xml/롬5:1
* https://2kstde4150.execute-api.ap-northeast-1.amazonaws.com/dev/v1/find/single/롬5:1

## dynamodb access구간 추가
* 매번 call 할 때마다 file 9mb를 모두 읽는 것이 느려서 개선하기로 함
