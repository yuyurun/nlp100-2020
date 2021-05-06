import itertools

def parse_mecab(sen):
    l_sen = []
    for line in sen.split('\n'):
        if line == '':
            return l_sen

        (surface, attr) = line.split('\t')
        attr = attr.split(',')
        l_dic = {
            'serface': surface,
            'base': attr[6],
            'pos': attr[0],
            'pos1': attr[1] 
        }
        l_sen.append(l_dic)
        

fname = '../../data/neko.txt.mecab'
with open(fname) as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
results = [parse_mecab(line) for line in lines]

dousi = [[r['base'] for r in result if r['pos'] == '動詞'] for result in results]
print(list(itertools.chain.from_iterable(dousi)))