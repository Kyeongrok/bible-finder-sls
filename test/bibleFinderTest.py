import libs.bibleFinder as finder

res = finder.findBetween("민",3,5,13)

for re in res:
    print(re)
    print(re['index'], re['text'])


res2 = finder.findByBookAndChapter("민", 3)
print(len(res2))

