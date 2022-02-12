num=int(input('Enter a number: '))
n=num//2
name=input('Enter your 1st name: ')
name2=input('Enter your 2nd name: ')
name3=input('Enter your 3rd name: ')

l=len(name)
l1=len(name2)
l2=len(name3)
for i in range(n):
    print(' '*(n-i-1) + '* '*(i+1),end='')
    if num%2==0:
        print(' '*(2*(n-i-1)) + '* '*(i+1))
    else:
        print(' '*(2*(n-i)) + '* '*(i+1))


if num%2==0:
    if l%2==0:
        print('* '* ((num-l)//2) + ' '.join(name) + ' *'* ((num-l)//2))
    else:
        print('* '* ((num-l)//2) + ' '.join(name) + ' *'* (((num-l)//2)+1))
else:
    if l%2==0:
        print('* '* ((num-l)//2) + ' '.join(name) + ' *'* (((num-l)//2)+1))
    else:
        print('* '* ((num-l)//2) + ' '.join(name) + ' *'* ((num-l)//2))

if num%2==0:
    if l1%2==0:
        print('* '* ((num-l1)//2) + ' '.join(name2) + ' *'* ((num-l1)//2))
    else:
        print('* '* ((num-l1)//2) + ' '.join(name2) + ' *'* (((num-l1)//2)+1))
else:
    if l1%2==0:
        print('* '* ((num-l1)//2) + ' '.join(name2) + ' *'* (((num-l1)//2)+1))
    else:
        print('* '* ((num-l1)//2) + ' '.join(name2) + ' *'* ((num-l1)//2))

if num%2==0:
    if l2%2==0:
        print('* '* ((num-l2)//2) + ' '.join(name3) + ' *'* ((num-l2)//2))
    else:
        print('* '* ((num-l2)//2) + ' '.join(name3) + ' *'* (((num-l2)//2)+1))
else:
    if l2%2==0:
        print('* '* ((num-l2)//2) + ' '.join(name3) + ' *'* (((num-l2)//2)+1))
    else:
        print('* '* ((num-l2)//2) + ' '.join(name3) + ' *'* ((num-l2)//2))



for i in range(num,0,-1):
    print(' '* (num-i) + '* '*i)        


