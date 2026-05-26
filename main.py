y=0
contacts=[]
while(y==0):
    print("Menu")
    print("1-> For Input")
    print("2->For Display")
    print("3->For Delete")
    print("4->For Update")
    opt=int(input("Enter your option"))
    if(opt==1):
        name=input("Name")
        email=input("Email")
        mobile=input("Mobile")
        #print(name+" "+email+" "+mobile)
        contacts.append((name,email,mobile))
    if(opt==2):
        print(contacts)
    if(opt==3):
        i=int(input("Enter the index you want to delete"))
        del contacts[i]
    if(opt==4):
        i=int(input("Enter the index you want to update"))
        name=input("Name")
        email=input("Email")
        mobile=input("Mobile")
        contacts[i]=(name,email,mobile)
    y=int(input("Do you want to continue? press 0- for yes"))
    #print("Hello Software Development")