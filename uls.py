t = "HelloWorld12345@%%%%"
u, l, d, s = 0, 0, 0, 0

for i in range(len(t)):
    if t[i].isupper():
        u += 1
    elif t[i].islower():
        l += 1
    elif t[i].isdigit():
        d += 1
    else:
        s += 1

print('upper case letters:', u, '\nlower case letters:', l, '\ndigits:', d, '\nspecial characters:', s)
