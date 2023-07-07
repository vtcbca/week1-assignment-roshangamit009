
x=int(input('Enter a Number :'))
temp=x
rev=0
if(int(x)):
    print('This is Integer')
else:
    print('This is Not Integer')
while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
if(temp==rev):
    print('The Number is a Palindrome')
else:
    print('The Number is Not Palindrome')
