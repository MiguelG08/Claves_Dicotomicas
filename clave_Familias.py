#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:26:23 2021

@author: miguel
"""


Dhoja = input("Hojas alternas: ")
if Dhoja == "si":
    estipulas = input("Tiene estipulas: ")
    if estipulas == "si":
        Testipulas = input("estipulas pequeñas y caducas: ")
        if Testipulas == "si":
            print("Malvaceae")
        else:
            hoja = input("Hojas simples: ")
            if hoja == "si":
                simetriahoja = input("hojas de base asimetrica: ")
                if simetriahoja == "si" :
                    print("Begoniaceae")
                else:
                    print ("Passifloraceae y urticaceae")
            else:
                print("Passifloraceae y fabaceae")
    else:
        hoja = input("Hojas simples: ")
        if hoja == "si":
            print ("solanaceae: ")
elif Dhoja == "no":
    estipulas = input("Tiene estipulas: ")
    if estipulas == "si":
        print ("Rubiaceae, urticaceae")
    else:
        hoja = input("Hojas simples: ")
        if hoja == "si":
            print ("Melastomataceae y acanthaceae")
        else :
            print("")