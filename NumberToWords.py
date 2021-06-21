words=[""," One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine"," Ten"," Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen"," Sixteen"," Seventeen"," Eighteen"," Nineteen"]
tens=[""," Ten"," Twenty"," Thirty"," Forty"," Fifty"," Sixty"," Seventy"," Eighty"," Ninety"]

def inHundred (x):
    h=x//100
    hwords=""
    if h>0:
        hwords+=words[h]+" Hundred"
    t=(x%100)
    if t<20:
        hwords+=words[t]
    else:
        hwords+=tens[t//10]+words[t%10]
    return hwords

def numToText(num):
    
    text=""
    billions=num//1000000000
    remainder=num%1000000000
    if billions > 0:
        text+=inHundred(billions)+" Billion"
        
    millions=remainder//1000000
    remainder=remainder%1000000
    if millions > 0:
        text+=inHundred(millions)+" Million"
        
    thousands=remainder//1000
    remainder=remainder%1000
    if thousands > 0:
        text+=inHundred(thousands)+" Thousand"
        
    text+=inHundred(remainder)

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
