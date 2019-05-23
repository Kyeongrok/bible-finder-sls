import json
import libs.bibleFinder as bf
from urllib.parse import unquote
from libs.htmlMaker import makeTr


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
        "body": "<html><body>{} {}</body></html>".format(index, result['text'])
    }
    return response
