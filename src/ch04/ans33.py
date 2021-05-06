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
        
def take_meisiku(sen):
    """
    単語の形態素解析結果のリストをもらって、「の」で繋がっている名詞句を抽出する
    """

    norn = ''
    l_norn = []
    for w in sen:
        if w['pos'] == '名詞':
            if norn == '':
                norn = w['serface']
            elif norn[-1] == 'の':
                norn += w['serface']
                l_norn.append(norn)
                norn = ''
            else:
                norn = ''
        elif w['serface'] == 'の' and norn != '':
            norn += 'の'
        else:
            norn = ''
    
    return l_norn
        



fname = '../../data/neko.txt.mecab'
with open(fname) as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
results = [parse_mecab(line) for line in lines]

ans = [take_meisiku(result) for result in results]
print(list(itertools.chain.from_iterable(ans)))