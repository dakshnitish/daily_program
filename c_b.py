import random
print('welcome to the cow and bull game')
#secret number
s_n = str(random.randint(10,99))
rem_chance = 7
cow = 0
bull = 0
while rem_chance > 0:
        g_n = input('enter the two digit number : ')
        if s_n == g_n:
            print('yay you guessed it right, you won!')
            break 
        else:     
            if g_n[0] == s_n[0]:
              bull += 1
            if g_n[1] == s_n[1]:
              bull += 1
            if g_n[0] == s_n[1]:
              cow += 1
            if g_n[1] == s_n[0]:
              cow += 1
            print('Bulls:',bull) 
            print('Cows:',cow)  
            rem_chance -= 1              

            if rem_chance < 1:
                print('sorry you ran out of maximum chance so you lost!')    



