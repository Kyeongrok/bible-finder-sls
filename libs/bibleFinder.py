import json, re, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
file = open(ROOT_DIR + "/tree_gae.json")
bible = json.loads(file.read())


def parse_index(string):
    st_book_nm = re.compile('[가-힣]{1,2}').findall(string)[0]
    r2 = re.compile('[0-9].+').findall(string)[0].split(':')
    chapter = r2[0]
    verse = r2[1]
    return st_book_nm, chapter, verse


def findByIndex(index):
    st_book_nm, chapter, verse = parse_index(index)
    idx = f'{st_book_nm}{chapter}:{verse}'

    # print(idx)
    result = {'st_book_nm': st_book_nm, 'chapter': chapter,
              'verse': verse, 'text': bible[st_book_nm][chapter][verse]}
    return result


def findBetween(st_book_nm, chapter: int, verse_from: int, verse_to: int):
    result = []
    filtered_chapter = bible[st_book_nm][str(chapter)]
    for i in range(verse_from, verse_to + 1):
        form = {'st_book_nm': st_book_nm, 'chapter': chapter, 'verse': i, 'index':f'{st_book_nm}{chapter}:{i}', 'text': filtered_chapter[str(i)]}
        result.append(form)

    return result


def findByChapter(shortendBookName, chapter):
    result = list(filter(lambda x: (x['shortendBookName'] == shortendBookName
                                    and x['chapter'] == chapter
                                    )
                         , bible))
    return result
