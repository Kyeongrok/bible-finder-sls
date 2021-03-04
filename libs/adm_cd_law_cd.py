import json, re, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dic = json.loads(open('tree_law_adm.json').read())

def make_tree(adm_law_codes):
    tre = {}
    for i in range(len(adm_law_codes)):
        spl = adm_law_codes[i].replace('\n','').split(',')
        # spl에서 2개 3개 나머지를 자른다.
        fst = spl[1][:2]
        snd = spl[1][2:5]
        trd = spl[1][5:]

        print(fst, snd, trd, type(fst))
        if tre.get(fst) == None:
            tre[fst] = {}
        if tre[fst].get(snd) == None:
            tre[fst][snd] = {}
        if tre[fst].get(snd).get(trd) == None:
            tre[fst][snd][trd] = spl[0]

    return tre


def get_adm_code(law_code):
    try:
        f = law_code[:2]
        s = law_code[2:5]
        t = law_code[5:]
        print(f, s, t)
        adm_code = dic[f][s][t]
        return adm_code
    except Exception as e:
        print('error---', law_code)
        return None

print(get_adm_code("1111051000"))
