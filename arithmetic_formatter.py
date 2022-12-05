def arithmetic_arranger(problems, results=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    newlist = list()
    for problem in problems:
        newlist.append(problem.split())

    firstRaw = list()
    secRaw = list()
    thirdRaw = list()
    fourthRaw = list()
    for op in newlist:
        # Cheching the operator :
        if op[1] != "+" and op[1] != "-":
            return "Error: Operator must be '+' or '-'."

        # Checking if the numbers aren't long
        if len(op[0]) > 4 or len(op[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Checking if the operands contain only digits and calculating
        try:
            if op[1] == "+":
                result = int(op[0]) + int(op[2])
            if op[1] == "-":
                result = int(op[0]) - int(op[2])
        except:
            return "Error: Numbers must only contain digits."

        # Arranging for the display :
        if len(op[0]) < len(op[2]):
            dif = len(op[2]) - len(op[0]) + 2
            spaces = " " * dif
            op[0] = spaces + op[0] + "    "
            op[2] = op[1] + " " + op[2] + "    "
            result = ((len(op[2]) - 4 - len(str(result))) * " ") + str(result) + "    "
            firstRaw.append(op[0])
            secRaw.append(op[2])
            thirdRaw.append((len(op[2]) - 4) * "-" + "    ")
            fourthRaw.append(result)
            continue

        if len(op[0]) > len(op[2]):
            dif = len(op[0]) - len(op[2])
            spaces = " " * dif
            op[2] = op[1] + " " + spaces + op[2] + "    "
            op[0] = "  " + op[0] + "    "
            result = ((len(op[2]) - 4 - len(str(result))) * " ") + str(result) + "    "
            firstRaw.append(op[0])
            secRaw.append(op[2])
            thirdRaw.append((len(op[2]) - 4) * "-" + "    ")
            fourthRaw.append(result)
            continue

        else:
            op[0] = "  " + op[0] + "    "
            op[2] = op[1] + " " + op[2] + "    "
            result = ((len(op[2]) - 4 - len(str(result))) * " ") + str(result) + "    "
            firstRaw.append(op[0])
            secRaw.append(op[2])
            thirdRaw.append((len(op[2]) - 4) * "-" + "    ")
            fourthRaw.append(result)

    # Removind the unnecessary spaces
    firstRaw[len(firstRaw) - 1] = firstRaw[len(firstRaw) - 1].rstrip()
    secRaw[len(secRaw) - 1] = secRaw[len(secRaw) - 1].rstrip()
    thirdRaw[len(thirdRaw) - 1] = thirdRaw[len(thirdRaw) - 1].rstrip()
    fourthRaw[len(fourthRaw) - 1] = fourthRaw[len(fourthRaw) - 1].rstrip()

    # Assembling list items into one string
    firstRaw = "".join(firstRaw)
    secRaw = "".join(secRaw)
    thirdRaw = "".join(thirdRaw)
    fourthRaw = "".join(fourthRaw)

    # concatenating the strings into one with new lines
    if results == True:
        arranged_problems = (
            firstRaw + "\n" + secRaw + "\n" + thirdRaw + "\n" + fourthRaw
        )
    elif results == False:
        arranged_problems = firstRaw + "\n" + secRaw + "\n" + thirdRaw

    return arranged_problems
