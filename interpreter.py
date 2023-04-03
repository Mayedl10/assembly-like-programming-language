import textwrap

def interpret(file):
    with open(file) as f:
        instructions_ = f.read().splitlines()
    f.close()

    instructions = []

    for i in instructions_:                             # instructions now looks like this: [['0000', '1010', '0110'], ['0110', '0111', '0111', '1111']]
        instructions.append(textwrap.wrap(i, 16))

    program_counter = 0
    run = True
    #print(instructions)

    registers = [0]*16
    memory = [0]*65536

    while run:
        #print(instructions)
        match instructions[program_counter][0]:
            case "0000000000000000":        #AND 
                dest = int(instructions[program_counter][1], 2)
                if int(instructions[program_counter][2], 2) and int(instructions[program_counter][3], 2):
                    registers[dest] = 1
                else:
                    registers[dest] = 0

            case "0000000000000001":        #ORR
                dest = int(instructions[program_counter][1], 2)
                if int(instructions[program_counter][2], 2) or int(instructions[program_counter][3], 2):
                    registers[dest] = 1
                else:
                    registers[dest] = 0

            case "0000000000000010":        #NOT
                dest = int(instructions[program_counter][1], 2)
                if int(instructions[program_counter][2], 2):
                    registers[dest] = 0
                else:
                    registers[dest] = 1

            case "0000000000000011":        #XOR
                dest = int(instructions[program_counter][1], 2)
                a = registers[int(instructions[program_counter][2], 2)]
                b = registers[int(instructions[program_counter][3], 2)]

                if (a and not b) or (not a and b):
                    registers[dest] = 1
                else:
                    registers[dest] = 0

            case "0000000000000100":        #ADD
                dest = int(instructions[program_counter][1], 2)
                a = registers[int(instructions[program_counter][2], 2)]
                sum = registers[dest]+a

                if sum > 65535 or sum < 0:
                    print("[ERROR:2] Sum out of range [0,65535]")
                    run = False
                
                registers[dest] = sum
            
            case "0000000000000101":        #SUB
                dest = int(instructions[program_counter][1], 2)
                a = registers[int(instructions[program_counter][2], 2)]
                diff = registers[dest]-a

                if diff > 65535 or diff < 0:
                    print("[ERROR:2] Difference out of range [0,65535]")
                    run = False
                
                registers[dest] = diff



            case "0000000000000110":        #MUL
                dest = int(instructions[program_counter][1], 2)
                a = registers[int(instructions[program_counter][2], 2)]
                product = registers[dest]*a

                if product > 65535 or product < 0:
                    print("[ERROR:2] Product out of range [0,65535]")
                    run = False
                
                registers[dest] = product



            case "0000000000000111":        #DIV
                dest = int(instructions[program_counter][1], 2)
                a = registers[int(instructions[program_counter][2], 2)]
                quot = registers[dest]//a

                if quot > 65535 or quot < 0:
                    print("[ERROR:2] Quotient out of range [0,65535]")
                    run = False
                
                registers[dest] = quot

            case "0000000000001000":        #PNL
                print()

            case "0000000000001001":        #JIZ                               
                dest = int(instructions[program_counter][1], 2)
                a = registers[int(instructions[program_counter][2], 2)]
                if a == 0:
                    program_counter = dest -1






            case "0000000000001010":        #LDI
                dest = int(instructions[program_counter][1],2)
                val = int(instructions[program_counter][2],2)
                registers[dest] = val



            case "0000000000001011":        #LOD (mem -> reg)
                dest = int(instructions[program_counter][1], 2)
                memaddr = int(instructions[program_counter][2], 2)

                registers[dest] = memory[memaddr]

            case "0000000000001100":        #STR (reg -> mem)
                dest = int(instructions[program_counter][2], 2)
                regaddr = int(instructions[program_counter][1], 2)

                memory[dest] = registers[regaddr]




            case "0000000000001101":        #PCI
                dest = int(instructions[program_counter][1], 2)
                out = registers[dest]
                print(chr(out), end = "")




            case "0000000000001110":        #INP
                dest = int(instructions[program_counter][1], 2)
                val = int(input())
                if not(val in range(0,65535)):
                    print("[ERROR:2] Input integer out of range [0,65535]")

                registers[dest] = val

            
            case "0000000000001111":        #HLT
                run = False
    





















            case other:
                print("[ERROR:1] Invalid binary operation", instructions[program_counter])

        
        program_counter += 1


