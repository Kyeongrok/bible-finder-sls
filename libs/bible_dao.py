import boto3, time, re

class BibleDao:
    def __init__(self, mode='DEV'):
        super().__init__()
        if mode == 'PRD':
            self.dynamodb = boto3.resource('dynamodb', verify=False)
        else:
            self.dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

    def parse_index(string):
        st_book_nm = re.compile('[가-힣]{1,2}').findall(string)[0]
        r2 = re.compile('[0-9].+').findall(string)[0].split(':')
        chapter = r2[0]
        verse = r2[1]
        return st_book_nm, chapter, verse
       
    def insert_a_row(self, table_name, row):
        dynamodb = self.dynamodb
        table = dynamodb.Table(table_name)
        r = table.put_item(Item=row)
        print(r)
    
    def read_rows(self, table_name, q):
        dynamodb = self.dynamodb
        table = dynamodb.Table(table_name)

        try:
            r = table.get_item(Key=q)
            return r['Item']
        except Exception as e:
            print(e.response['Error']['Message'])

    def find_by_chapter(self,  chapter):
        dynamodb = self.dynamodb
        table = dynamodb.Table('Book')
        response = table.query(
            KeyConditionExpression=Key('chapter').eq(chapter)
        )
        return response['Items']

if __name__ == '__main__':
    dao = BibleDao('PRD')
    b = {
        'chapter':'김1',
        'verse':2,
        'text':'bye'
    }
    print(dao.read_rows('Book', {'chapter':'창1', 'verse':1} ))
    

