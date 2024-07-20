row = int(input("Enter rows: "))
column = int(input("Enter columns: "))
char = input("Enter character to display: ")

for x in range(row):
    for j in range(column):
        print(char, end="")
    print()

#While Loop 
i = 0
j = 0
while i<row:
    while j<=i:
        print(char, end="")
        j+=1
    i+=1
    j=0
    print()

#doWHile Loop
print("DO while")
a = row
b = 0
while True:
    while True:
        print(char, end="")
        if b<a:
            b+=1
        else:
            break
    if a > 0:
        b = 0
        a -= 1
        print()
    else:
        break