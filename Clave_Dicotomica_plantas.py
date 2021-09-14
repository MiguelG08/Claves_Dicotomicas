#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:13:03 2021

@author: miguel
"""
hojas_opuestas = input("¿tiene hojas opuestas?")
if hojas_opuestas == "si" :
    corteza_exfoliante = input("¿tiene corteza exfoliante?")
    if corteza_exfoliante == "si" :
        print ("myrthaceae")
    else:
        print("rubiaceae")
else:    
   hojas_alternas = input("¿tiene hojas alternas?")      
   if hojas_alternas == "si" :
       print("zigiveraceae")
   else:
       espadice= input("¿tiene inflorecencia en espadice?")
       if espadice == "si":
           print ("araceae")