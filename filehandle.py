def write_contact(data):
    with open('contact_data','w') as file:
        for item in data:
            line=item[0]+"#"+item[1]+"#"+str(item[2])+"\n"
            file.write(line)
def read_contact():
    contact_data=[]
    with open('contact_data','r') as file:
        for line in file:
            k=line.strip()
            s=k.split("#")
            contact_data.append((s[0],s[1],s[2]))
    return contact_data
