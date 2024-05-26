maior=0
menor=0 
for i in range(1,6):
    n=float(input(f'Digite o da {i}° pessoa peso: '))
    if maior<=n or i==1:
        maior=n
    if menor>=n or i==1:
        menor=n
print(f'O mais pesado foi {maior}Kg')
print(f'O mais leve foi {menor}Kg')