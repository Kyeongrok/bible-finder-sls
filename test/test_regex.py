import re
vv = '삼하113'

index = re.search('[가-힣]{1,2}', vv).group(0)

print(index)

addr = '삼하113:2-5'
book_chapter, verses = addr.split(':')
verseFrom, verseTo = verses.split('-')

print(book_chapter)