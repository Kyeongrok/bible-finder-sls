import libs.bibleFinder as finder
import json

def test_single():

    r = finder.findByIndex('롬5:5')
    print(r)
    pass

test_single()

# test_single()
def make_tree():
    t = {}
    for row in finder.bible:
        if t.get(row['shortendBookName']) == None:
            t[row['shortendBookName']] = {}

        if t[row['shortendBookName']].get(row['chapter']) == None:
            t[row['shortendBookName']][row['chapter']] = {}

        if t[row['shortendBookName']][row['chapter']].get(row['verse']) == None:
            t[row['shortendBookName']][row['chapter']][row['verse']] = {}

        t[row['shortendBookName']][row['chapter']][row['verse']] = row['text']

    with open('libs/tree_gae.json', 'w+') as f:
        f.write(json.dumps(t))


