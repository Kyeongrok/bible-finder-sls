# Serverless로 만든 API Server

## Serverless Framework설치

- npm있으면 설치 할 수 있습니다.

```
npm install -g serverless
```

위 명령어로 serverless framework을 먼저 설치 해주세요.

## sls 배포
* sls deploy --stage dev
* sls deploy function -f findSingle

## request요청
* https://2kstde4150.execute-api.ap-northeast-1.amazonaws.com/dev/v1/find/single/xml/롬5:1
* https://2kstde4150.execute-api.ap-northeast-1.amazonaws.com/dev/v1/find/single/롬5:1

## dynamodb access구간 추가
* 매번 call 할 때마다 file 9mb를 모두 읽는 것이 느려서 개선하기로 함
