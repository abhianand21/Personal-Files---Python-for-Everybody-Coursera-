hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Enter numeric number')
    quit()

if h <= 40:
    print(h * r)
else :
    i = h % 40
    print(((h-i) * r) + (i * r * 1.5))
