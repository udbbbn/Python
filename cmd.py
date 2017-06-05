import subprocess

cmd = 'cmd.exe'
begin = 1
end = 200
while begin < end:
    
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.stdin.write('ping 10.3.16.' + str(begin) + "\n")
    
p.stdin.close()
p.wait()
    
print('execution result:%s'%p.stdout.read())