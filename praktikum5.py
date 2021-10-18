# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:16:55 2021

@author: jofi
"""




n = '0'
t = 0
j = 0
while (n != ''):
    n = str(input('Masukkan Nilai : '))
    t += 1
    if (n== '') :
        break 
    elif (n == 'A') :
        print('Nilai = 4.00')
        j += 4.00
    elif (n == 'A-') :
        print('Nilai = 3.75')
        j += 3.75
    elif (n == 'B+'):
        print('Nilai = 3.50')
        j += 3.50
    elif (n == 'B'):
        print('Nilai = 3.00')
        j += 3.00
    elif (n == 'B-') :
        print('Nilai = 2.75')
        j += 2.75
    elif (n == 'C+') :
        print('Nilai = 2.50')
        j += 2.50
    elif (n == 'C') :
        print('Nilai = 2.00')
        j += 2.00
    elif (n == 'C-') :
        print('Nilai = 1.75')
        j += 1.75
    elif (n == 'D') :
        print('Nilai = 1.50')
        j += 1.50
    elif (n == 'E'):
        print('Nilai = 1.25')
        j += 1.25
    else :
        print('Tolong Masukkan Nilai Yang Benar!')
        
rata = j/(t-1)
print('Rata Ratanya adalah', rata)
        
        
        
        
        