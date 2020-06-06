#import subprocess,os

#subprocess.call(["ls","-al"])
#subprocess.call(["ls","-al"])
#s=subprocess.call(["exit 10"], shell=True)
#print s
#d=os.system('echo "s"')
#print d


import subprocess
import time

def d():
    x = 5#some amount of seconds
    delay = 1.0
    timeout = int(x / delay)

    args = ["sleep 10"] #a string or array of arguments
    task = subprocess.Popen("sleep 2", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print "task",task
#task1 = task.communicate()
#print "task1",task1
#while the process is still executing and we haven't timed-out yet
    while task.poll() is None and timeout > 0:
        #do other things too if necessary e.g. print, check resources, etc.
        time.sleep(delay)
        timeout -= delay
        #return False
        print"ask.poll()",task.poll()
        if task.poll() == 0:
            task1 = task.communicate()
            print "task1",task1
            return True
    return False
#task1 = task.communicate()
#print "task1",task1
print"d",d()
