from sys import path

import material2_package.modulo
from material2_package import modulo
from material2_package.modulo import *

# from material2_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(material2_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)