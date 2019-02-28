# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:49:26 2019

@author: MaddySravs
"""

PropertyPrice = [150000, 225000, 190000, 275000, 300000, 250000, 330000, 180000, 350000, 400000]
DownPayment = [40000, 80000, 50000, 50000, 75000, 60000, 85000, 40000, 90000, 100000]
MortgageAmt = [100000, 100000, 150000, 200000, 250000, 200000, 300000, 60000, 300000, 350000]

## Function to calculate 'LTV'
def LTV(MortgageAmt, PropertyPrice):
    LTV = math.ceil(MortgageAmt/PropertyPrice * 100)
    print(LTV)
LTV(100000, 150000)    
LTV(100000, 225000)
LTV(150000, 190000)
LTV(200000, 275000)
LTV(250000, 300000)
LTV(200000, 250000)
LTV(300000, 330000)        
LTV(60000, 180000)
LTV(300000, 350000)
LTV(350000, 400000)

## Function to Calcualte 'Rating'
def rating(LTV):
    if LTV > 80:
        print("High")
    elif 60 <= LTV <=80:
        print("Medium")
    elif 40 <= LTV <=59:
        print("Low")
    elif LTV < 40:
        print("Very Low")
rating(67)
rating(45)
rating(79)
rating(73)
rating(84)
rating(80)
rating(91)
rating(34)
rating(86)
rating(88)

## Function to define 'Extrafee'
def Extrafee(rating):
    if rating == "High":
        print("Extra fee is 10%")
    elif rating == "Medium":
        print("Extra fee is 8%")
    elif rating == "Low":
        print("Extra fee is 6%")
    elif rating == "Very Low":
        print("Extra fee is 4%")
Extrafee("Medium")
Extrafee("Low")
Extrafee("Medium")
Extrafee("Medium")
Extrafee("High")
Extrafee("Medium")
Extrafee("High")
Extrafee("Very Low")
Extrafee("High")
Extrafee("High")