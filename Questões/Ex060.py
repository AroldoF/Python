n = int(input("Digite um número: "))
c = 0
new = 1
print(f"\033[34mResolvendo {n}!\033[m")
while c < n - 1:
    new *= n - c
    print(f"{n-c} x ", end="")
    c += 1
print(f"1 = {new}")

# for i in range(n,1,-1):
#    new*=i
#    print(new)
