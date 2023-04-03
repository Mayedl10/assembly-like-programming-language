import os

def decToBin(num):
    binary_str = bin(int(num))[2:]
    padded_str = binary_str.rjust(16, '0')
    return padded_str



def assemble(file):
    new_name = os.path.basename(file).split(".")[0] + ".bin"

    with open(file) as f:
        content = f.readlines()
    f.close()

    tokens = []

    for i in content:
        tokens.append(i.split(" "))
    
    del content, f

    for sublist in tokens:
        for string in range(len(sublist)):
            sublist[string] = sublist[string].replace("\n", "")



    output = ""

    
    position = 0
    run = True
    while run:
        match tokens[position][0]:
            case "AND":
                output += "0000000000000000"
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])
                addr2 = decToBin(tokens[position][3])

                output += dest
                output += addr1
                output += addr2
                output += "\n"


            case "ORR":
                output += "0000000000000001"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])
                addr2 = decToBin(tokens[position][3])

                output += dest
                output += addr1
                output += addr2
                output += "\n"

            case "NOT":
                output += "0000000000000010"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])

                output += dest
                output += addr1
                output += "\n"

            case "XOR":
                output += "0000000000000011"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])
                addr2 = decToBin(tokens[position][3])

                output += dest
                output += addr1
                output += addr2
                output += "\n"

            case "ADD":
                output += "0000000000000100"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])

                output += dest
                output += addr1
                output += "\n"

            case "SUB":
                output += "0000000000000101"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])

                output += dest
                output += addr1
                output += "\n"

            case "MUL":
                output += "0000000000000110"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])

                output += dest
                output += addr1
                output += "\n"

            case "DIV":
                output += "0000000000000111"                
                dest = decToBin(tokens[position][1])
                addr1 = decToBin(tokens[position][2])

                output += dest
                output += addr1
                output += "\n"

            case "PNL":
                output += "0000000000001000"
                output += "\n"

            case "JIZ":
                output += "0000000000001001"
                dest = decToBin(tokens[position][1])
                a = decToBin(tokens[position][2])
                
                output += dest
                output += a
                output += "\n"

            case "LDI":
                output += "0000000000001010"
                dest = decToBin(tokens[position][1])
                val = decToBin(tokens[position][2])

                output += dest
                output += val
                output += "\n"

            case "LOD":
                output += "0000000000001011"
                regaddr = decToBin(tokens[position][1])
                memaddr = decToBin(tokens[position][2])

                output += regaddr
                output += memaddr
                output += "\n"

            case "STR":
                output += "0000000000001100"
                memaddr = decToBin(tokens[position][1])
                regaddr = decToBin(tokens[position][2])

                output += regaddr
                output += memaddr
                output += "\n"

            case "PCI":
                output += "0000000000001101"
                regaddr = decToBin(tokens[position][1])

                output += regaddr
                output += "\n"

            case "INP":         #inp  regdest
                output += "0000000000001110"
                dest = decToBin(tokens[position][1])

                output += dest
                output += "\n"

            case "HLT":
                output += "0000000000001111\n"


            case "END":
                run = False   


            case other:
                print(f"[ERROR:3] Invalid instruction")
                run = False

        position += 1

    
    if not(os.path.exists(new_name)):
        f = open(new_name, "x+")   #create file
    f = open(new_name, "w")    #open file
    f.write(output)            #write to file
    f.close()                  #close file


#assemble(os.path.join("files", "test.asm"))