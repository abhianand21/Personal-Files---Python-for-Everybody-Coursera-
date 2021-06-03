#we're going to work on right now is in Chapter five and it is exercise one.
#We're going to repeat asking for a number until the word done is entered, and then we're going to print the total.
#Then, we're going to print the count, and then we're going to print the average at the end.
#We're going to enter some numbers and I'm going to do some error checking, and we're going to keep on going.

num = 0
tot = 0.0

while True :
    sval = input('Enter a number')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print('Invalid input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print('All Done')
print(num, tot, tot / num)
    
