import json
import libs.bibleFinder as bf
from urllib.parse import unquote
from libs.htmlMaker import makeTr
from libs.htmlMaker import makeTable
import html.parser


# sls 배포
# sls deploy --stage prod --aws-profile matprod --profile matprod
def wrap(result):
    response = {
        "statusCode": 200,
        "headers":{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'text/html; charset=utf-8'
        },
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

def findSingle(event, context):
    addr = unquote(event['pathParameters']['addr'])
    result = bf.findByIndex(addr)
    return wrap(result)



def findSingleXml(event, context):
    addr = unquote(event['pathParameters']['addr'])
    result = bf.findByIndex(addr)[0]
    unescaped = html.unescape(result['text'])

    index = "{}{}:{}".format(result['shortendBookName'], result['chapter'], result['verse'])
    response = {
        "statusCode": 200,
        "headers":{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'text/html; charset=utf-8'
        },
        "body": "<html><body>{} {}</body></html>".format(index, unescaped)
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

def makeRessponse(jsonContent):
    response = {
        "statusCode": 200,
        "headers":{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps(jsonContent)
    }
    return response

def getChapter(event, context):
    queryStringParameters = event['queryStringParameters']

    book = queryStringParameters['book']
    chapter = queryStringParameters['chapter']
    result = bf.findByChapter(book, int(chapter))

    return makeRessponse(result)


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

# https://jxkjd9ecxh.execute-api.ap-northeast-2.amazonaws.com/dev/v1/find/election21/full
def findElection21Full(event, context):
    queryStringParameters = event['queryStringParameters']
    q_from = queryStringParameters['from']
    q_to = queryStringParameters['to']
    # queryString can be used after
    file = open('./static/election21.json')
    list = json.loads(file.read())
    # temporary select top 100 because lambda memory is low
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json; charset=utf-8'
        },
        "body": json.dumps({
            "data":list[int(q_from):int(q_to)],
            "paging":{"total":len(list)}
        })
    }
    return response