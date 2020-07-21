#Exercise 5.3.1
def is_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        print("Yes")
    else:
        print("No")

#Exercise 5.3.2
def test_triangle():
    a = int(input("Type a and hit enter\n"))
    b = int(input("Type b and hit enter\n"))
    c = int(input("Type c and hit enter\n"))
    is_triangle(a,b,c)

test_triangle()