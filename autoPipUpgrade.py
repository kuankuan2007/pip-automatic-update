import os,tempfile,sys,time
screenOut=[]
os.system("@echo off")
fileName="ghmPipUpgrade.tmp"
tempdir=tempfile.gettempdir()+"\\"
print("正在启动...",end="")
screenOut.append("正在启动...")
blacklist=["xlrd"]
def reSetScreen():
    os.system("cls")
    for i in screenOut:
        print(i)
try:
    print("\r正在获取更新列表...")
    screenOut[-1]="正在获取更新列表..."
    os.system("pip list --outdate >"+tempdir+fileName)
    with open(tempdir+fileName) as file:
        lines=file.readlines()
        if len(lines)<2:
            screenOut.append("无更新内容")
            print("无更新内容")
        else:
            flag=0
            screenOut.append("正在启动更新")
            screenOut.append("共"+str(len(lines)-2)+"项,正在更新第1项")
            print("正在启动更新,共"+str(len(lines)-2)+"项...")
            print("共"+str(len(lines)-2)+"项,正在更新第1项")
            for i in range(0,len(lines)):
                
                if lines[i][:2]=="--":
                    flag=1
                    continue
                if flag==0:continue
                screenOut[-i+1]="共"+str(len(lines)-2)+"项,正在更新第"+str(i-1)+"项"
                reSetScreen()
                packageName=lines[i][:lines[i].find(" ")]
                if packageName in blacklist:
                    screenOut.append("    第"+str(i-1)+"项:跳过更新 "+packageName)
                    print("    第"+str(i-1)+"项:跳过更新 "+packageName)
                    continue
                screenOut.append("    第"+str(i-1)+"项:正在更新 "+packageName+" ...")
                print("    第"+str(i-1)+"项:正在更新 "+packageName+" ...")
                os.system("pip install --upgrade "+packageName)
                screenOut[-1]+="[done]"
            screenOut.append("已完成所有更新")
except BaseException as err:
    print(str(err.__class__.__name__)+"\n"+str(err))
    screenOut.append(str(err.__class__.__name__)+"\n"+str(err))
finally:
    time.sleep(0.5)
    reSetScreen()
    #os.remove(tempdir+fileName)
    os.system("pause")