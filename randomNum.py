from random import randint
file = open("test.bin", "w")


result = ""
for i in range(800):
    rannum = randint(0,1)
    result = str(result) + str(rannum)

file.write(result)
