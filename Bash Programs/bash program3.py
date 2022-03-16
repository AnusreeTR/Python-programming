import subprocess
res=subprocess.run(['echo','welcome to India'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
print(res.stdout)
