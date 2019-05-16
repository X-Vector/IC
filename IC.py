'''
# Reference
# https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC.html
'''

import sys
try:
    cipher_file = sys.argv[1]
    cipher = open(cipher_file).read().lower()
    letter = "abcdefghijklmnopqrstuvwxyz"
    sum = 0.0
    data = []
    for i in letter:
        for j in cipher:
            if i == j:
                sum+=1
        data.append(sum)
        sum = 0.0

    sum = 0.0
    for i in data:
        sum += i

    n = sum * (sum - 1)
    sum = 0.0
    for i in data:
        if i != 0:
            sum += i * (i - 1)
    if n != 0 :
        IC = sum / n
        print "IC = ",IC
        if IC >= 0.040 and IC <= 0.055:
            print "Index of Coincidence =",IC
            print "The Message has Probably Been Crypted Using a Vigenere cipher"
        elif IC >= 0.01 and IC < 0.040:
            print "Index of Coincidence =",IC
            print "Similar To a Random Text, Then The Message has Probably Been Crypted Using a Polyalphabetic Cipher"
        elif IC > 0.055 and IC < 1:
            print "Index of Coincidence =",IC
            print "The Message has Probably Been Crypted Using a Transposition Cipher or a Monoalphabetic Substitution"
        else :
            print "Can't Define The Cipher"
        
    else:
        print "Can't Define The Cipher"
except IndexError:
    print "Usage : python", sys.argv[0] ,"cipher_file"
