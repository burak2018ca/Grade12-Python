 
def Dice_Odds_Dictionary():
    Dictionary = {}

    for x in range (1, 7):
        for y in range(1,7):
            Total = x + y
            Dice_Tuple = (x,y)
            
            Dictionary.setdefault(Total, []).append(Dice_Tuple)

    print("Keys | Length")
    print("---------------")
    for x in Dictionary.keys():
        print (str(x) + "    |    " + str(len(Dictionary [x])))


Dice_Odds_Dictionary()