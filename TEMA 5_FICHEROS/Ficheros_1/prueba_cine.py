from cine import *

if __name__ == "__main__":
    c = Cine([3,4,5,5,5])
    print(c)
    c.ocupar(2,"A")
    c.ocupar(2,"B")
    c.ocupar(2,"C")
    print(c)
    c.desocupar(2,"A")
    print(c)