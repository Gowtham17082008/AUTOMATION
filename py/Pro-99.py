import os
import shutil

'''os.mkdir("C:/Users/admin/Desktop/python-Guess-Number-Game-master/swapna")
os.getcwd()

mypath="C:/Users/admin/Desktop/python-Guess-Number-Game-master/swapna"
isexist= os.path.exists(mypath)
print(isexist)

mypath="C:/Users/admin/Desktop/python-Guess-Number-Game-master/test.txt"
root=os.path.splitext(mypath)
print("root path=",root[0])
print("extension path=",root[1])

mypath="C:/Users/admin/Desktop/python-Guess-Number-Game-master/test.txt"
mydestintion="C:/Users/admin/Desktop/class-98/test2.txt"
copy=shutil.move(mypath,mydestintion)'''

mypath=input("Enter path")
list=os.listdir(mypath)
for i in list:
    name,ext=os.path.splitext(i)
    ext=ext[1:]
    if ext =="":
        continue

    if os.path.exists(mypath + "/" + ext):
        shutil.move(mypath+"/"+ i,mypath+"/"+ext+"/"+i)
    else:
        os.makedirs(mypath+"/"+ext)
        shutil.move(mypath+"/"+ i,mypath+"/"+ext+"/"+i)