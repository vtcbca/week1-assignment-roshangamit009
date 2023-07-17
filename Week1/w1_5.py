#Write a python script to enter any string and count vowel.
str=input('Enter A String :')
vow=0
for i in str:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
        vow=vow+1
print('Number of Vowels Are :')
print(vow)

        
