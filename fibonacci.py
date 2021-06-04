#Taking the number of input size from the user and looping until the input size
for _ in range(int(input())):
    #Assigning the input character string to variable s
    s=input()
    d={}
    #Using dictionary d counting the number of occurance of letters in the string
    for i in s:
        if(i in d):
            d[i]+=1 
        else:
            d[i]=1 
    #Storing the occurance of letters in list l and sorting the list
    l=[]
    for i in d.values():
        l.append(i)
    l.sort()
    print(l)
    #Outputing the result i.e Dynamic or Not Boolean value 
    if(len(l)<3):
        print("Dynamic")
    else:
        if(l[-1]==l[-2]+l[-3]):
            print("Dynamic")
        else:
            print("Not")
            