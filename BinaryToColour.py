file = open("test.bin", "r")
line = file.readlines(0)
line = line[0]

def validation(line):
    if len(line) % 2 != 0:
        line = line + "0"
    if len(set(line)) == 2 and "0" in set(line) and "1" in set(line):
        print("")
    else:
        print("Incorrect Value")
        exit()

def main(line):
    validation(line)
    colours_Array = []
    for i in range(0,len(line),2):
        match ("{}{}").format(line[i],line[i+1]):
            case "00":
                colours_Array.append("BLACK")
            case "01":
                colours_Array.append("WHITE")
            case "10":
               colours_Array.append("RED")
            case "11":
                colours_Array.append("GREEN")
    print(colours_Array)
    return colours_Array

if __name__ == '__main__':
    main(line)

