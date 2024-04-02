
#need 2 text file with some 2-3 word writen on it

import math as m
import string as s

def freq(f):
    l = open(f, 'r').read()
    w = l.translate(str.maketrans(s.punctuation + s.ascii_uppercase, " " * len(s.punctuation) + s.ascii_lowercase)).split()
    fr = {}
    for i in w:
        fr[i] = fr[i] + 1 if (i in fr) else 1
    print("File", f, ":", len(l), "lines,", len(w), "words,", len(fr), "distinct words")
    return fr

def dp(d1, d2):
    d = 0.0
    for i in d1:
        if i in d2:
            d += (d1[i] * d2[i])
    return d

sl1 = freq('hello.txt')
sl2 = freq('world.txt')

print("distance between documents is ", m.acos(dp(sl1, sl2) / m.sqrt(dp(sl1, sl1) * dp(sl2, sl2))), "radians")
