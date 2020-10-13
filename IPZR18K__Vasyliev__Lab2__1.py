engine__program = True
while engine__program == True:
    info = "Hello user.\nThis program help you simular division unicellular ameba for a certain time."
    condition = "\nEvery 3 hour  happens unicellular ameba division for a two cells.\n3 hour = 2 unicellular ameba."
    print(info)
    print(condition)
    ameba = 1
    amebaCount = []
    amebaCount.insert(0, str(ameba))
    print(f"\nSequence division simular division at the beginning of the day --> {amebaCount}\n")
    for hour in range(0, 27, 3):
        ameba *= 2
        amebaCount.append(str(ameba))
        print(f"Sequence division simular division --> {amebaCount}")
        if hour == 24:
            print(f"\nSequence division simular division at the end day--> {amebaCount}")
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
