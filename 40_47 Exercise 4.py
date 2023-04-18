""""Exercise-->4"""
import random
import string
'''# its wrong after hardwork of 2 hours
try:

    print("1) Sending message.\n2) Decode Message.")
    i=int(input("Enter input\t"))

    match(i):
        case 1:

            a = input("Enter Message : ")
            b = []
            c = ""
            if(len(a)>2):
                for i in a:
                    # print(i)
                    b.append(i)
                # print(b)

                b.insert(len(b), b[0])
                b.pop(0)
                # print(b)

                suffix = ''.join(random.choices(string.ascii_letters, k=3))
                # print(suffix)
                prefix = ''.join(random.choices(string.ascii_letters, k=3))
                # print(prefix)

                c = ''.join(b)
                print(f"{prefix}{c}{suffix}")
            else:
                print(a[::-1])

        case 2:
            a= input("Enter message for decode : ")
            if(len(a)>2):
                b=a[3:-3]
                c=b[len(b)-1]+b[:len(b)-1]
                print(c)
            else:
                print(a[::-1])
        case _:
            print("\n\nEnter Valid value between 1 and 2.")
            print("1) Sending message.\n2) Decode Message.")
            i=int(input("Enter input\t"))

except ValueError:
    print("\n\nEnter Integer Value!!!")



# if(i>=1 or i<3):
#     raise ValueError("Choose valid value between 1 and 2")
# print(i)

'''
# print(r1)
# print(r1)
coding = int (input("1 for coading and 2 for decoading ."))
pr="coding" if coding==1 else "Decoading"
st=input((f"Enter message for {pr} : "))
words = st.split(" ")

coding= True if (coding==1) else False
if (coding):
    nword=[]
    for word in words:
        if (len(word)>3):
            r1 = ''.join(random.choices(string.ascii_letters, k=3))
            r2= ''.join(random.choices(string.ascii_letters, k=3))
            stnew= r1+word[1:] +word[0]+r2
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))

else:
    nword = []
    for word in words:
        if (len(word) >= 3):

            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))