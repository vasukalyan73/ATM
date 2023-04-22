import random
a=random.choice(['rock','paper','scissor'])
uc = input('enter the choice :')
print(a,uc)
if a!=uc:
    if a=='rock' and uc=='paper':
        print('rock is win')
    elif a=='paper' and uc=='scissor':
        print('scissor is win')
    elif a=='scissor' and uc=='rock':
        print('rock is win')
else:
    print('tie')