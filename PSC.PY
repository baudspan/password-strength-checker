import string

password='Sudeepa@2006'
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

charecters=[upper_case,lower_case,special,digits]

length= len(password)

score=0

with open('password.txt','r') as f:
    common=f.read().splitlines()
if password in common:
    print('password found in common list: 0/7')
    exit()

if length>8:
    score+=1
if length>12:
    score+=1
if length>17:
    score+=1
if length>20:
    score+=1

print(f'password length is {str(length)},adding {str(score)} points')

if sum(charecters)>1:
    score+=1
if sum(charecters)>2:
    score+=1
if sum(charecters)>3:
    score+=1

print(f'password has {str(sum(charecters))} differnt charecter type, adding {str(sum(charecters)-1)} points!')

if score<4:
    print(f'password is weak score:{str(score)}/7')
elif score==4:
    print(f'password is ok score:{str(score)}/7')
elif score>4 and score<6:
    print(f'password is fine score:{str(score)}/7')
elif score>6:
    print(f'password is strong score:{str(score)}/7')
