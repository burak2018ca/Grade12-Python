import datetime

def Create_Date_Dictionary():

    Date_Dictionary = {}

    for x in range(1, 13):
        Month_long = datetime.date(1900, x, 1).strftime("%B")
        Month_short = datetime.date(1900, x, 1).strftime("%b").upper()
        
        Date_Dictionary [Month_short] = Month_long

    return Date_Dictionary

def Date_Decoder(date, dictionary):

    Filtered_Date = date.split("-")

    Day = Filtered_Date[0]
    Month = Filtered_Date[1].upper()
    Year = "19" + Filtered_Date[2]  

    
    if (Month in dictionary):
        Date_tuple = (Day, dictionary[Month], Year)
    else:
        return "Incorrect entry"

    return Date_tuple
