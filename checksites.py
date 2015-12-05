import re
f=open("postResp_output.txt")
f2=open("sites_run.txt")
f3=open("sites_run_throwerror.txt",'w')
f4=open("sites_run__nocookie.txt",'w')
x=f.read()
for i in f2:
    i=i.rstrip("\n")
    if(not re.search(i,x)):
        i+="\n"
        f3.write(i)
    else:
        i+="\n"
        f4.write(i)
    
f.close()
f2.close()
f3.close()
f4.close()
