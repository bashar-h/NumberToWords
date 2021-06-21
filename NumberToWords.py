words=[""," One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine"," Ten"," Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen"," Sixteen"," Seventeen"," Eighteen"," Nineteen"]
tens=[""," Ten"," Twenty"," Thirty"," Forty"," Fifty"," Sixty"," Seventy"," Eighty"," Ninety"]

def inHundred (x):
    h=x//100
    hw=""
    if h>0:
        hw=words[h]+" Hundred"
    t=(x%100)
    if t<20:
        tw=words[t]
        nw=""
    else:
        tt=t//10
        tw=tens[tt]
        nw=words[t%10]
    return hw+tw+nw

def numToText(num):
    
    billionsWords=""
    millionsWords=""
    thousandsWords=""
    hundredsWords=""

    billions=num//1000000000
    remainder=num%1000000000
    if billions > 0:
        billionsWords=inHundred(billions)+" Billion"

    millions=remainder//1000000
    remainder=remainder%1000000
    if millions > 0:
        millionsWords=inHundred(millions)+" Million"

    thousands=remainder//1000
    remainder=remainder%1000
    if thousands > 0:
        thousandsWords=inHundred(thousands)+" Thousand"

    hundredsWords=inHundred(remainder)
    text=billionsWords+millionsWords+thousandsWords+hundredsWords

    if text=="":
        text="Zero"
    else:
        text=text[1:]

    return(text)

repeat="Y"

while repeat.upper()=="Y":
    num=int(input("\nInput a number: "))
    print ("\n>> The number is",numToText(num))
    repeat=input("\nTo convert a new number enter 'Y' or press ENTER to exit: ")
