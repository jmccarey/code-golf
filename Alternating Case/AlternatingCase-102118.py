"""b=True
n=""
s="stop mocking me"
for c in s:
    if b:
        n+=c.upper()
    else:
        n+=c
    b=not b

print(n)
"""

#''.join([x.upper()if s.index(x)%2else x for x in s])


#x=''.join;x(map(x,list(zip(s[::2].upper(),s[1::2]))))

#''.join(map(lambda x,y:x+y,s[::2].upper(),s[1::2]))


#''.join(map("{}{}".format,s[::2].upper(),s[1::2]))

s="stop mocking me."
n=list(s);n[::2]=s[::2].upper();''.join(n)







