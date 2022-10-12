from time import sleep
import os

def cadastro():
    while True:
        try:
            nome = str(input('nome: '))
            idade = int(input('idade: '))
            arquivo1 = open('dados.txt', 'a+')
        except ValueError:
            print('ERRO NO CADASTRO! a idade deve ser um número. ')
        except FileNotFoundError:
            arquivo1  = open('dados.txt', 'w')
            arquivo1.write(f'{nome} ')
            arquivo1.write(f'{str(idade):>20}\n')
            print(f'registro de {nome} adicionado com sucesso;')
            sleep(1)
            break
        else:
            arquivo1.write(f'{nome:<30} ')
            arquivo1.write(f'{str(idade) + " anos"}\n')
            print(f'registro de {nome} adicionado com sucesso')
            sleep(1)
            break


def limparDados():
    os.remove('dados.txt')
    print('dados removidos com sucesso.')
    sleep(1)
