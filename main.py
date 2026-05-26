from helper import *
from filehandle import *
y=0
rdata=read_contact()
set_contacts(rdata)
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
    if(y!=0):
        kdata=get_contacts()
        write_contact(kdata)