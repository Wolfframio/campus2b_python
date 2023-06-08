# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:20:00 2023

@author: german
"""

while True:
    try:
        x = int(input("Introduce un número: "))
        a = 10 / x
        break

    except ZeroDivisionError: #Excepción a manejar de tipo valor.
        print("¡Vaya! Has introducido un 0")
        
    except: #Excepción a manejar de tipo valor.
        print("¡Vaya! No has introducido un número")