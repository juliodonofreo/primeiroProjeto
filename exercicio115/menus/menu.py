from time import sleep

def menus():
    print('-' * 20)
    print('MENU PRINCIPAL'.center(20))
    print('-' * 20)
    print('1- ver pessoas cadastradas')
    print('2- cadastrar uma pessoa')
    print('3- limpar dados')
    print('4- sair')
    while True:
        try:
            retorno = int(input('digite aqui: '))
        except ValueError:
            print('favor digitar um número. ', end='')
        else:
            if retorno < 1 or retorno > 4:
                print('por favor digite um valor entre 1 e 3. ', end ='')
            else:
                return retorno


def ver():
    try:
        arquivo1 = open('dados.txt')
        print('-'*40)
        print('PESSOAS CADASTRADAS'.center(40))
        print('-'*40)
        print(arquivo1.read())
        sleep(1)
    except:
        print('você ainda não cadastrou ninguém.')
        sleep(1)
