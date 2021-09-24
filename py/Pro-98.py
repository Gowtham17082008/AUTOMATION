f=open("test.txt", 'r')
print(f.read())
print(f.readline(4))
print(f.readlines())

f=open("test.txt","w") 
f.write("This is the form file 2 ")


f=open("test.txt2","w") 
f.write("This is the form file 1 ")


'''takeinput=input("type your fav color")
if(takeinput=="black"):
    print("its black")
elif(takeinput=="red"):
    print("its red")
else:
    print("nice choice")'''
