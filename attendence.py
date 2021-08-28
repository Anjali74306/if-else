total=int(input("enter the total number of classes held"))
attended=int(input("enter the number of classes attend"))
percent=(attended*100)/total
if percent>=75 :
    print( "your attendence is ",percent, ("% you are  allow for examination"))
    if percent<75:
        print("you are not  allow for exam")
    else:
        print("all the best foe exam")
else:
    print("best of luck")


    




 