olds=input('Enter Any String :')
char=input('Enter a character to replace all vowal with it :')
new=''
for i in range(len(olds)):
    if olds[i]=='a' or olds[i]=='A' or olds[i]=='e' or olds[i]=='E' or olds[i]=='i' or olds[i]=='I' or olds[i]=='o' or olds[i]=='O' or olds[i]=='u' or olds[i]=='U' :
        new=new+char
    else:
        new=new+olds[i]

print('\nOriginal String :',olds)
print('\nNew String :',new)
