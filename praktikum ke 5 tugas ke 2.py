# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:46:35 2021

@author: jofin
"""

u = "0"
t = 0
while (u != ""):
    u = input("Masukkan Umur: ")
    if u != '':
        umur_penonton = int(u)
        if umur_penonton <= 2:
            print("Gratis")
            harga = 0
        elif umur_penonton >= 3 and umur_penonton <= 12:
            print("Harga $14.00")
            harga = 14
        elif umur_penonton >= 65:
            print("Harga $18.00")
            harga = 18
        else:
            print("Harga $23.00")
            harga = 23  
        t = t + harga
        print("Running total: %0.2f" % t)
        
j = int(input("masukkan jumlah uang: "))
jawaban = j - t
print("Running kembalian: %0.2f" % jawaban)
        