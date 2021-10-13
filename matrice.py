from itertools import islice
i=(''.join(open('input.txt').readlines())).split()
n=int(i[-1])
i=list(islice(i, n))
t=[]
x=dp=ds=sdp=jdp=sds=jds=0
y=n-1
for j in i: t.append(list(eval(j))[:n])
for p in range(n): dp+=t[p][p]
while y>-1:
    ds+=t[x][y]
    x+=1
    y-=1
for y in range(n):
    for x in range(y+1,n):
        sdp+=t[y][x]
        jdp+=t[x][y]
coef=n-1
for y in range(n):
    for x in range(coef):
        sds+=t[x][y]
    coef-=1
x=n-1
for y in range(1,n):
    for j in range(y):
        x-=j
        jds+=t[y][x]
        x=n-1
print('     Matricea:',*t, f'     Operatiile matematice efectuate:\nSuma pe diagonala principala: {dp}\nSuma pe diagonala secundara: {ds}\nSuma elementelor mai sus de diagonala principala: {sdp}\nSuma elementelor mai jos de diagonala principala: {jdp}\nSuma elementelor mai sus de diagonala secundara: {sds}\nSuma elementelor mai jos de diagonala secundara: {jds}', sep='\n')