import json
import libs.bibleFinder as bf
from urllib.parse import unquote
from libs.htmlMaker import makeTr
from libs.htmlMaker import makeTable

# sls 배포
# sls deploy --stage prod --aws-profile matprod --profile matprod

def findSingle(event, context):
    addr = unquote(event['pathParameters']['addr'])
    result = bf.findByIndex(addr)
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def findSingleXml(event, context):
    addr = unquote(event['pathParameters']['addr'])
    result = bf.findByIndex(addr)[0]

    index = "{}{}:{}".format(result['shortendBookName'], result['chapter'], result['verse'])
    response = {
        "statusCode": 200,
        "headers":{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": "<html><body>{} {}</body></html>".format(index, result['text'])
    }
    return response

def findBetween(event, context):
    queryStringParameters = event['queryStringParameters']

    book = queryStringParameters['book']
    chapter = queryStringParameters['chapter']
    verseFrom = queryStringParameters['verseFrom']
    verseTo = queryStringParameters['verseTo']
    verses = bf.findBetween(book, int(chapter), int(verseFrom), int(verseTo))

    response = {
        "statusCode": 200,
        "headers":{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps(verses)
    }
    return response


def findBetweenXml(event, context):
    queryStringParameters = event['queryStringParameters']

    book = queryStringParameters['book']
    chapter = queryStringParameters['chapter']
    verseFrom = queryStringParameters['verseFrom']
    verseTo = queryStringParameters['verseTo']
    verses = bf.findBetween(book, int(chapter), int(verseFrom), int(verseTo))
    response = {
        "statusCode": 200,
        "headers":{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": makeTable(verses)
    }
    return response
