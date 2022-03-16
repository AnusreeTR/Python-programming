import subprocess
res=subprocess.run(['cat','Anusree.txt'],stderr=subprocess.PIPE,text=True)
print(res.stderr)
