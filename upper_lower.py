def counts(str):
    uppercase = ""
    lowercase = ""
    for i in str.strip():
        if i.isupper():
            uppercase=uppercase +i
            
        elif i.islower():
            lowercase=lowercase+i

    print(len(uppercase))
    print(len(lowercase))

str = input("enter the string:")
counts(str)