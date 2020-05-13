# Serverless로 만든 API Server

## sls 배포
sls deploy --stage prod --aws-profile matprod --profile matprod

## requirements.txt 만들기
pip freeze > requirements.txt

## lambda만들 때 주의할 점
1. function에는 event, context두개의 parameter를 넘겨야 한다.
2. python의 모듈을 추가 했기 때문에 docker가 필요함
3. 처음 받으면 npm init도 해줘야 함

