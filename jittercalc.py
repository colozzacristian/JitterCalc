import math
import sys

def main(argv):
    avg=0
    jitter=0
    argv.pop(0)
    for i in range(0,len(argv)):
        argv[i]=float(argv[i])
        avg+=argv[i]
    avg=avg/(len(argv))
    print("averange: ",avg)
    for i in range(0,len(argv)):
            jitter+=((argv[i]-avg)**2)
    print("jitter(less precise): ",math.sqrt(jitter/(len(argv))))    
    print("jitter: ",math.sqrt(jitter/(len(argv)-1)))
       
      
main(sys.argv)
