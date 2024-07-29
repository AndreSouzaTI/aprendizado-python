#Testando print;

print('\nPython na Escola de Programação da Alura\n')



#Testando separador(sep);
print('A','N','D','R','E\n',sep='\n')

#Testando imput, variáveis e junção em String;
nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos\n')

#Testando junção e arredondamento;
pi = 3.14159
pi = print(f'O valor redondo de pi é: {pi:.2f}\n')

#Testando if else elif
numero = int(input('Insira um número: '))
if numero % 2 == 0:
    print('O número é par!')
else:
    print('O número é impar!')    

idade = int(input('Insira sua idade: '))
if 0 < idade <= 12:
    print('Criança!')
elif 12 < idade < 18:
    print('Adolescente!')
elif idade >= 18:
    print('Adulto!')
else:
    print('Valor inválido!')

usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")


#Trabalhando com Listas

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_nomes = ['André', 'Luana', 'Henry', 'Victória']
lista_de_anos = [1987, 2024]

def lista_numeros():
    for numero in lista_de_numeros:
        print(numero)

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += 1
print(soma_impares)     

for i in range(10, 0, -1):
    print(i)

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")





