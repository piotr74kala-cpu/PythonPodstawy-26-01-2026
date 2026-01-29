# import fun8
#
# print(fun8.all_params(1, 2, 3, 4))


from pakiet import fun

fun.powitanie()

import pakiet.fun as pk  # alias

pk.powitanie()

import pakiet

# pakiet.powitanie() # AttributeError: module 'pakiet' has no attribute 'powitanie'
pakiet.info()  # dopisane w __init__.py
# Wersja v1.789.01.23
