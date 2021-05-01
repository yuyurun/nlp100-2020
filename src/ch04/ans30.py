
with open('../../data/neko.txt.mecab') as f:
    lines = f.readlines()
l_doc = []
l_sen = []
for line in lines:
    if line != 'EOS\n' and line != '\n':
        result = line.split('\t')
        l_result = result[1].split(',')
        l_dic = {
            'serface': result[0],
            'base': l_result[6],
            'pos': l_result[0],
            'pos1': l_result[1] 
        }
        l_sen.append(l_dic)
    elif line == 'EOS\n':
        l_doc.append(l_sen)
        l_sen = []
    
print(l_doc[:3])