import time

t=time.strftime('%H:%M:%S')
print(t)

# hrs=time.strftime('%H')
# print("Hours : ",hrs)
# min=time.strftime('%M')
# print("Minutes : ",min)
# sec=time.strftime('%S')
# print("Seconds : ",sec)

# hrs= int(input(time.strftime('%H')))
hrs=int(input("enter hors"))
print(hrs)

if (hrs>=0 and hrs<12):
    print("Good morning vedant sir.")
elif (hrs>=12 and hrs<16):
    print("Good afternoon vedant sir.")
elif (hrs>=16 and hrs<20):
    print("Good evening vedant sir.")
elif (hrs>=20 and hrs<24):
    print("Good night vedant sir.")

else:# it used for taking input by user.
    print("You entered invalid value\nTime between 0 to 24.")