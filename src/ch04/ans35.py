import itertools
import numpy as np
import collections

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

results = [[r['serface'] for r in result] for result in results]
results = list(itertools.chain.from_iterable(results))

c = collections.Counter(results)
print(list(np.array(c.most_common()).T[0]))