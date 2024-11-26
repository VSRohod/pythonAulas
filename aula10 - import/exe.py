import importlib

import exe_m

print(exe_m.variavel)

for i in range(10):
    importlib.reload(exe_m)
    print(i)

print('Fim')