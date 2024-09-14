tamanho=int(input("Qual o tamanho da base?"))
c=0
for i in range(tamanho,0,-1):
    for j in range(0,i):
        print(c, end=" ")
        c+=1
        if c>9:
            c=0
    print("")

for i in range(2,tamanho):
    for j in range(0,i):
        print(c, end=" ")
        c+=1
        
    if c==9:
        c=0
    print("")