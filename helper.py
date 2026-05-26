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
def get_contacts():
    return contacts
def set_contacts(cdata):
    global contacts
    contacts=cdata