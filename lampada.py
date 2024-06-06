"""
Se apertar interruptor 1(I1), lampada A desliga ou liga
caso apertar o interruptor 2(I2), ambas as lampadas A e B
Trocam de estado (liga ou desliga)
"""
#Definição das variáveis
N = int(input())
A=0
B=0
if 2<=N<=100000:
    for num in range(N):
        apertos = int(input())
        if apertos == 1 and A == 0:
            A = 1 
        elif apertos == 1 and A == 1:
            A = 0
        elif apertos == 2 and A == 0 and B == 0:
            A = 1
            B = 1
        elif apertos == 2 and A == 1 and B == 1:
            A = 0
            B = 0
        elif apertos == 2 and A == 0 and B == 1:
            A = 1
            B = 0
        elif apertos == 2 and A == 1 and B == 0:
            A = 0
            B = 1
        else:
            A = 0
            B = 0
print(A,B)