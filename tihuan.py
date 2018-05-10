aStr="Hello, World!"
bStr=aStr[:7]+"Python!"
print(bStr)
count=0
for ch in bStr[:]:
    if ch in ',.!?':
        count+=1
print(count)