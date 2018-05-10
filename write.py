f1=open('C:/Users/asus/Desktop/new.txt')
#f.write("hello,I'm your father!")
cNames=f1.readlines()
for i in range(0,len(cNames)):
    cNames[i]= str(i+1)+' '+cNames[i]
f1.close()
f2=open('C:/Users/asus/Desktop/new2.txt','r+')
f2.writelines(cNames)
f2.close()
f=open('C:/Users/asus/Desktop/new2.txt','r+')
txt=f.read()
print(txt)
f.close()


