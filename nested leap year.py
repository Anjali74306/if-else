year=int(input("enter the year"))
if year%4==0:
    print("this is leap year")
    if year%100==0:
        print("it a century")
    else:
        print("it is not a century")
else:
    print("aree aap pgl ho kya ye bhi nhi pta")

