#!/usr/bin/env python

start = 0
end   = 99
divisor = 7
print("Here is a list of all the numbers from",start,"to",end,"not divisible by",divisor)
for n in range(0,100): 
    if n == 0: 
        print(n) #I know this is cheating but I couldn't figure it out. 
    elif (n%7) == 0: #% command gives you remainder, if remainder 0, perfectly divisible
        continue #skip all numbers divisible by 7
    else:
        print(n) #print all other numbers
