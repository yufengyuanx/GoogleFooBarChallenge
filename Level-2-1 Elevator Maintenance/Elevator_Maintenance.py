def answer(l):
    l.sort(key=lambda a : [int(b) for b in a.split('.')])
    return l
