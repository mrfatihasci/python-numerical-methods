## The following code is written by Fatih Asci

m=0
piNum=0.0
Num=0.0
for n in range(0, 10000000):
    if piNum>(3.141)and piNum<(3.142):
        m=n
        break
    piNum+=(4.0*float((-1)**n))/(((2.0)*n)+1)

for k in range(0, m):
    Num+=(4.0*float((-1)**k))/(((2.0)*k)+1)
print(Num)
print(m)
