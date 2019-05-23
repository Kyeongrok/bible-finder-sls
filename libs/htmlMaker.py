def makeTr(verse):
    index = "{}{}:{}".format(verse['shortendBookName'], verse['chapter'], verse['verse'])
    return "<tr><td>{}</td><td>{}</td></tr>".format(index, verse['text'])


def makeTable(verses):
    head = "<html><body><table>"
    tbody = ""
    for verse in verses:
        tbody = tbody + makeTr(verse)
    tail = "</table></body></html>"
    return head + tbody + tail
