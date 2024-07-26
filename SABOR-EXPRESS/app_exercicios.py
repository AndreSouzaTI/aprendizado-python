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