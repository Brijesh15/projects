import os,sys
path = os.path.dirname(os.path.abspath(__file__)).split('Python')[0]
print(path)
print(os.system('export PATH=$PATH:%s'%path))
print(path)
