from uncompyle6.main import decompile
import marshal, time, sys, os

def decompile_python_3():
    file_name = input('[*] Decompile marshal python 3.x\n[?] File output: ')
    with open(file_name + '.py', 'wb') as f:
        x = marshal.loads(open('marcode.py3', 'rb').read())
        decompile(3.7, x, f)
    print(f'\n[result] Saved as {file_name}.py')

def decompile_python_2():
    file_name = raw_input('[*] Decompile marshal python 2.x\n[?] File output: ')
    with open(file_name + '.py', 'wb') as f:
        x = marshal.loads(open('marcode.py2', 'rb').read())
        decompile(2.7, x, f)
    print(f'\n[result] Saved as {file_name}.py')

if sys.version_info[0] < 3:
    decompile_python_2()
else:
    decompile_python_3()