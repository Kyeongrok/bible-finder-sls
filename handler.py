import json, re
import libs.bibleFinder as bf
from libs.bibleFinder import parse_index
import libs.bible_dao as bdao
from urllib.parse import unquote
from libs.htmlMaker import makeTr
from libs.htmlMaker import makeTable
import html.parser

dao = bdao.BibleDao('PRD')


# sls 배포
# sls deploy --stage prod --aws-profile matprod --profile matprod
def wrap(result):
    response = {
        "statusCode": 200,
        "headers": {
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
    result = bf.findByIndex(addr)
    unescaped = html.unescape(result['text'])

    index = "{}{}:{}".format(result['shortendBookName'], result['chapter'], result['verse'])
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'text/html; charset=utf-8'
        },
        "body": "<html><body>{} {}</body></html>".format(index, unescaped)
    }
    return response


def findBetween(event, context):
    addr = unquote(event['pathParameters']['addr'])

    #시113:1-2
    book_chapter, verses = addr.split(':')
    verseFrom, verseTo = verses.split('-')
    book = re.search('[가-힣]{1,2}', book_chapter).group(0)
    chapter = re.search('[0-9]{1,3}', book_chapter).group(0)
    verses = bf.findBetween(book, int(chapter), int(verseFrom), int(verseTo))

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps(verses)
    }
    return response


def makeRessponse(jsonContent):
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps(jsonContent)
    }
    return response


def find_between_xml(event, context):
    queryStringParameters = event['queryStringParameters']

    book = queryStringParameters['book']
    chapter = queryStringParameters['chapter']
    verse_from = queryStringParameters['verseFrom']
    verse_to = queryStringParameters['verseTo']
    verses = bf.findBetween(book, int(chapter), int(verse_from), int(verse_to))
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": makeTable(verses)
    }
    return response


def find_single_fr_db(event, context):
    addr = unquote(event['pathParameters']['addr'])
    st_book_nm, chapter, verse = parse_index(addr)
    chapter = f'{st_book_nm}{chapter}'
    r = dao.read_rows('Book', {'chapter': chapter, 'verse': int(verse)})
    return wrap(json.loads(r))

def getChapter(event, context):
    queryStringParameters = event['queryStringParameters']

    book = queryStringParameters['book']
    chapter = queryStringParameters['chapter']
    result = bf.findByChapter(book, int(chapter))

    return makeRessponse(result)

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
            "data": list[int(q_from):int(q_to)],
            "paging": {"total": len(list)}
        })
    }
    return response
