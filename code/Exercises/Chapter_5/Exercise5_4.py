def recurse(n,s):
    """This function performs the sum s+n+(n-1)+(n-2)+...+1 for NON-NEGATIVE n""" #This is Exercise 5.4.2
    if n == 0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(3,0)

#Exercise 5.4.1
#If n is negative, then we get an infinite loop. This is because the indexes n, n-1, n-2, ... never reach zero
#What the program does in this case is trying to sum s + n + (n-1) + (n-2) + ... until n reaches zero.

recurse(-1,0)
