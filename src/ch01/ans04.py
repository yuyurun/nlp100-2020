a = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# .,を除去
a = a.replace(',', '').replace('.', '')

a_dic = {}
id1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i,word in enumerate(a.split(' ')):
    if i+1 in id1:
        a_dic[word[0]] = i+1
    else:
        a_dic[word[0]+word[1]] = i+1

print(a_dic)
