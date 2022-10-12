import subprocess as sp

lines = ['x=5','f"{x=}"','print(x)']

proc = sp.Popen('python -i -q',stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT,universal_newlines=True,shell=True,bufsize=0)
# proc.stdin.write('\n'.join(lines))
# print(proc.stderr.readline())
# print(proc.stderr.readline())
# print(proc.stderr.readline())
# # print(proc.stderr.readline())
# # print(proc.stderr.readline())
# proc.kill()
cmd = proc.stdout.read(4)
proc.stdin.write(f'{lines[0]}\n')
cmd = proc.stdout.read(4)
while cmd!='>>> ':
    cmd += proc.stdout.readline()
# out,err = proc.communicate(lines[0]+'\n')
    print(cmd)
    cmd = proc.stdout.read(4)
# print(err)
print(cmd)
proc.kill()
