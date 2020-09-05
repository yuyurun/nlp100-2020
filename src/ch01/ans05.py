def create_ngram(text, n=2, mode='str'):
    """
    n-gramを作る

    Args:
        text(str) : 対象となる文
        n(int) : n-gramのn
        mode(str) : strかword 
    """
    if mode == 'str':
        l = [s for s in text]
    else:
        l = [s for s in text.split(' ')]
    return [''.join(l[i:i+n]) for i in range(len(l) - n + 1)]


if __name__ == '__main__':
    a = 'I am an NLPer'
    print(create_ngram(a))
    print(create_ngram(a, mode='word'))
