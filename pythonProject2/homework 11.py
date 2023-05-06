def fun(a,b):
    a=1
    b=0
    try:
        x=a/b
        ptint(x)
    except ZeroDivisionError:
            print ("ZeroDivisionError")
fun (0,1)

#2
def sum (a,b):
    try:
        x=a+b
        print(x)
    except TypeError:
        print (TypeError)

sum ("YES",5)