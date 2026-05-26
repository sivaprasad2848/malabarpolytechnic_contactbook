contacts=[]
def contact_create():
    name=input("Name")
    email=input("Email")
    mobile=input("Mobile")
    #print(name+" "+email+" "+mobile)
    contacts.append((name,email,mobile))
def contact_delete():
    i=int(input("Enter the index you want to delete"))
    del contacts[i]
def contact_list():
    print(contacts)
def contact_update():
    i=int(input("Enter the index you want to update"))
    name=input("Name")
    email=input("Email")
    mobile=input("Mobile")
    contacts[i]=(name,email,mobile)
def menu():
    print("Menu")
    print("1-> For Input")
    print("2->For Display")
    print("3->For Delete")
    print("4->For Update")
    op=int(input("Enter your option"))
    return op
y=0

while(y==0):
    opt=menu()
    if(opt==1):
        contact_create()
    if(opt==2):
        contact_list()
    if(opt==3):
        contact_delete()
    if(opt==4):
        contact_update()
    y=int(input("Do you want to continue? press 0- for yes"))
    #print("Hello Software Development")