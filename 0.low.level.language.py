# Python code to
# demonstrate readlines()

# L = ["Geeks\n", "for\n", "Geeks\n"]
 
# writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
 
# Using readlines()
file1 = open('entrada.txt', 'r')
Lines = file1.readlines()
file1.close()
 
# print(type(Lines))  # las lineas del texto en una lista de cadenas
# print(Lines)        # incluyendo el \n

for line in Lines:
    print(line,end="")

file2 = open('salida.txt', 'a')
file2.writelines(Lines)
file2.close()

count = 0
for line in Lines:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))
    print(f"{count}: {line.strip()}")

