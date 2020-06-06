import subprocess
import time
class file():
    
    def __init__(self, age):
        self.__age = age
        
   
    def _executeBashcmd(self, cmd):
        """
        """
        print "cmd is %s"% str(cmd)
        process = subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#        time.sleep(2)
#        res = process.communicate()
        print "returning process",process
        return process

class file1(file):
    
    def __init__(self):
        pass

f = file(12)
f._file__age = 15
print f._file__age 
#f = file1()
#cmd = 'cd /home/brijesh/Desktop/dr_imsless_ericsson && python file.py'
#f._executeBashcmd(cmd)
