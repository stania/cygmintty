import os, env
from subprocess import Popen, PIPE

env.setupVSEnv(100)

cmd = r'C:\cygwin\bin\mintty.exe -e /usr/bin/bash -c "STARTDIR=\"{}\" exec /bin/bash --login"'.format(os.getcwd())

Popen(cmd).wait()
