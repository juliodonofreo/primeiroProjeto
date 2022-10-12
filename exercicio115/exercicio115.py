from menus.menu import menus, ver
from dados.dados import cadastro, limparDados

while True:
    função = menus()
    if função == 1:
        ver()
    elif função == 2:
        cadastro()
    elif função == 3:
        limparDados()
    elif função == 4:
        break
print('até logo')
