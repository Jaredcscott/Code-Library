def bubbleSort(inputList):
    didSwap = True
    count = 0
    while didSwap:
        didSwap = False
        for i in range(len(inputList) - 1):
            if inputList[i].getCardValue() > inputList[i + 1].getCardValue():
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                cardList = generateCardList(inputList)
                count += 1
                print("%i: "%count, cardList)
                didSwap = True