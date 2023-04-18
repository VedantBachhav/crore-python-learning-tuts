list=["Which is the capital of india?","Who is father of indian navy?","who is PM of india?","Who is known as hitman in cricket?"]

ans=["Delhi","Chatrapati Shivaji Maharaj","Narendra modi","Rohit Sharma"]




print(list[0])
a = input("Type your answer : \n")

if a==ans[0]:
    print("Congratulations You won 10,000/- RS")
    print(list[1])
    a = input("Type your answer : \n")

    if(a==ans[1]):
        print("Congratulations You won 20,000/- RS")
        print(list[2])
        a = input("Type your answer : \n")

        if (a == ans[2]):
            print("Congratulations You won 50,000/- RS")
            print(list[3])
            a = input("Type your answer : \n")

            if (a == ans[3]):
                print("Congratulations You won 100,000/- RS")
            else:
                print("Wrong well played and so close\nBetter luck next time.")
        else:
            print("Wrong So, close\nBetter luck next time.")
    else:
        print("Wrong So, close\nBetter luck next time.")
else:
     print("Wrong\nBetter luck next time.")