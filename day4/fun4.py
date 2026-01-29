# funkcja wewnętrzna, zagnieżdżona

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2()
    return fun2 # zzwracamy adres funkcji, referencje


fun1()  # To jest fun1
# To jest fun1
# To jest fun2
print(fun1) # <function fun1 at 0x00000249FD2075E0>
xfun = fun1()
print(xfun) # <function fun1.<locals>.fun2 at 0x00000231A590B060>
print(type(xfun)) # <class 'function'>
xfun() # uruchomienie funkcji
xfun() # uruchomienie funkcji
xfun() # uruchomienie funkcji
xfun() # uruchomienie funkcji
xfun() # uruchomienie funkcji
xfun() # uruchomienie funkcji
# To jest fun2