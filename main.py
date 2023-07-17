# by cscheerer on GitHub
from time import sleep

testnumber = 0

for i in range(50):
    print("")

print("Begin typing (say the word print to print):")
print("")

list = [""]
lines = 0

while True:
    userinput = input("> ")
    lines += 1

    if userinput == "print":
        lines -= 1

        linetoprint = 0
        print(list[0])

        for i in range(50):
            print("")

        for i in range(lines):
            linetoprint += 1
            print(list[linetoprint])
            sleep(0.2)

        quit()

    else:
        list.append(userinput)


