"""
Se apertar interruptor 1(I1), lampada A desliga ou liga
caso apertar o interruptor 2(I2), ambas as lampadas A e B
Trocam de estado (liga ou desliga)
"""
N = int(input())
sequencia = list(map(int, input().split()))

luz_A = 0
luz_B = 0

for i in sequencia:
    if i == 1:
        luz_A = 1 - luz_A
    elif i == 2:
        luz_A = 1 - luz_A
        luz_B = 1 - luz_B

print(luz_A)
print(luz_B)
