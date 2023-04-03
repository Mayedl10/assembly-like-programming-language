import random
import interpreter
import assembler

def get_code(path:str):

    with open(path) as f:
        content = f.read().split(" ")

    f.close()

    code = []
    for i in content:
        code.append(i.split(" "))

    del content, f
    return code

def shell():

    run = True
    if random.randint(1,100000) == 69:
        silly = True
    else:
        silly = False

    while run:
        if silly:
            task = input("\n\_('o')_/ ").split(" ")
        else:
            task = input("\n>> ").split(" ")

        match task[0]:
            case "build":
                assembler.assemble(task[1])

            case "exec":
                interpreter.interpret(task[1])

            case "exit":
                run = False

            case "help":
                print("Commands:\nbuild ... converts assembly code to binary. IMPORTANT: WILL get stuck if there is not 'HLT' instruction!\nexec  ... executes a binary\nexit  ... closes the shell\nhelp  ... shows this menu")



            case other:
                print("[ERROR:0] invalid command")

if __name__ == "__main__":
    shell()