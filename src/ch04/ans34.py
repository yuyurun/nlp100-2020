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
        
def meisi_long(sen):
    """
    単語の形態素解析結果のリストをもらって、名詞の連結を最長一致を抽出する
    """

    norn = ''
    l_norn = []
    norn_count = 0
    for w in sen:
        if w['pos'] == '名詞':
            if norn == '':
                norn = w['serface']
                norn_count = 1
            else:
                norn += w['serface']
                norn_count += 1
        elif norn_count > 1:
            l_norn.append(norn)
            norn = ''
            norn_count = 0
        else:
            norn = ''
            norn_count = 0
            
    
    return l_norn
        



fname = '../../data/neko.txt.mecab'
with open(fname) as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
results = [parse_mecab(line) for line in lines]

ans = [meisi_long(result) for result in results]
print(list(itertools.chain.from_iterable(ans)))