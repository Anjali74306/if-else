print("welcome to hdfc bank","insert the card")
card=(input("choose card type:/rupay/visa/master/"))
if card=="rupay" or"visa" or "master":
    print("yes")
    language=(input("choose your language:/english/hindi/"))
    if language== "english" or "hindi" or "marathi":
        print("next step")
        options=(input("select prefer option:/withdrwal/check balance/change pin/"))
        if options=="withdrwal" or "check balance" or "change pin":
            print("wait")
            pin=int(input("enter your pin"))
            if pin<9999:
                print("your pin has been matched")
                amount=int(input("enter the amount"))
                if amount>500 and amount<10000:
                    print("please wait your transaction is being proceed")
                    reciept=(input("would yu like to take recipt:/yes/no"))
                    if reciept=="yes" or "no":
                        print("collect your card")
                    else:
                        print("please choose the yes or no")
                else:
                    print("please enter the amount availble")
            else:
                print("please enter correct pin")
        else:
            print("please select prefer option")
    else:
        print("please select your suitable language")
else:
    print("please choose type of card")







    


 
          