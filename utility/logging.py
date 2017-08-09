from . import registry as reg

f = open(reg.out_file, 'w')

def writeline(message):
    f.writelines(message + '\n')

def write(message):
    f.write(message)

def closeFile():
    f.close()