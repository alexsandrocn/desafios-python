import re

n = int(input())
while n:
    n -= 1
    placa = str(input())
    if re.match(r'^([A-Z]{3})-([0-9]{4})$', placa):
        try:
            r = int(placa[-1])
            if r > 8 or r == 0:
                print('FRIDAY')
            elif r > 6:
                print('THURSDAY')
            elif r > 4:
                print('WEDNESDAY')
            elif r > 2:
                print('TUESDAY')
            else:
                print('MONDAY')
        except:
            print('FAILURE')
    else:
        print('FAILURE')
