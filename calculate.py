#!/usr/bin/env python3
import sys
try:
   earning = int(sys.argv[1])
except:
   print("parameter Error")
#calculate the tax
m = earning-0-3500
if m<0:
   tax = 0
   print('{:.2f}'.format(tax))
elif m<=1500 and m>=0:
   tax = m*0.03
   print('{:.2f}'.format(tax))
elif m<=4500 and m>1500:
   m = m-1500
   tax = m*0.1+45
   print('{:.2f}'.format(tax))
elif m<=9000 and m>4500:
   m = m -4500
   tax = m*0.2+45+300
   print('{:.2f}'.format(tax))
elif m<=35000 and m>9000:
   m = m - 9000
   tax = m*0.25+45+300+900
   print('{:.2f}'.format(tax))
elif m<=55000 and m>35000:
   m = m-35000
   tax = m*0.3+45+300+900+6500
   print('{:.2f}'.format(tax))
elif m<=80000 and m >55000:
   m = m - 55000
   tax = m*0.35+45+300+900+6500+6000
   print('{:.2f}'.format(tax))  
else:
   m = m - 80000
   tax = m*0.45+45+300+900+6500+6000+8750
   print('{:.2f}'.format(tax))


