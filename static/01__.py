import json

file = open("./election21.json")

ss = json.loads(file.read())[:2000]

file2 = open('./election21_2000.json', 'w+')
file2.write(json.dumps(ss))