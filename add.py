import random
for i in range(5):
    a = int(random.random() * 200)
    b = int(random.random() * 200)
    print '{0}. Maayan how much is: {1}+{2}=?'.format(i,a,b)
    x=raw_input()
    if int(x) == a+b:
        print '?? ?????'
    else:
        print '?? ????'