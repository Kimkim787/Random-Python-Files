#kwargs -> Keyword Arguments => use keywords in arguments

def myfunc(**args):
    print("Hello ",args["name"], ". You are ", args["age"], "years old, studying", args["course"])

def datas(**data):
    print("Values are: ", end="")
    for keys,values in data.items():
        print(values, " ", end="")

def uhm(**par):
    for key,value in par.items():
        print(key, ":", value)

myfunc(name="Clement", age="21", course="BSIT")
datas(name="Clement", age="21", course="BSIT")

print()
uhm(name="Kaye", age="20", location="Canlawilao")