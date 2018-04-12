#Author:Erkang
age_of_oldboy=56

for i in range(3):
    guess_age=int(input('guess age:'))
    if age_of_oldboy==guess_age:
        print('yes,you got it!')
        break
    elif age_of_oldboy<guess_age:
        print('think small')
    else:
        print('think big')
else:
    print('fulk...')