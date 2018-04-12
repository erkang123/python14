#Author:Erkang
age_of_oldboy=56

count=0
while count<3:
    guess_age=int(input('guess age:'))
    if age_of_oldboy==guess_age:
        print('yes,you got it!')
        break
    elif age_of_oldboy<guess_age:
        print('think small')
    else:
        print('think big')
    count +=1
    if count==3:
        countinue_guess=input('do you want to keep guessing ...?')
        if countinue_guess!='n':
            count=0
else:
    print('fulk...')