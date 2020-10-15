engine__program = True
while engine__program == True:

    message = "This program help transform your string which you enter reverse in order"
    print("%s\n" % message)
    userText = input("Enter you string, please: ").lower().split()
    userTextStr = " ".join(userText)
    print("Your string which the you enter (format: line): %s" % userTextStr)
    print("Your string which the you enter (format: list): %s\n" % userText)

    rvsText = []
    size = -len(userText)
    i = -1;

    while i >= size:
        rvsText.append(userText[i])
        i -= 1

    resultStr = " ".join(rvsText)
    print("\nYour reverse string which the you entered (format: line): %s" % resultStr)
    print("Your reverse string which the you entered (format: list): %s" % rvsText)
    exitLoop = True
    while exitLoop == True:
        engine__program = input("\nIf you want to retry enter 1.\nIf you want exit enter 0.\n")
        if engine__program == '1':
            exitLoop = False
            engine__program = True
        elif engine__program == '0':
            exit(0)
        else:
            exitLoop = True
