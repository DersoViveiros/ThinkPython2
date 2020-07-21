#Exercise 5.2.1
def check_fermat(a,b,c,n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    if n>2 and a>0 and b>0 and c>0 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")

#Exercise 5.2.2
def prompting_fermat():
    a = int(input('Type a and hit enter\n'))
    b = int(input('Type b and hit enter\n'))
    c = int(input('Type c and hit enter\n'))
    n = int(input('Type n and hit enter\n'))
    check_fermat(a,b,c,n)

prompting_fermat()