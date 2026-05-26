try:
    print("Line1")
    print("Line2")
    print("Line3")
    raise Exception("There is an exception occured")
    print("Line4")
    print("Line5")
    print("Line6")
    print("Line7")
except Exception as e :
    print("There is an exception occured")
