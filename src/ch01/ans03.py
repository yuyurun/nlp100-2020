a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# .,を除去
a = a.replace(',', '').replace('.', '')

print([len(w) for w in a.split(' ')])
