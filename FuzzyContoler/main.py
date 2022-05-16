import numpy as np
import sympy as sy
rules = np.array([['low', 'negative', 'optimal','low','low','low','ac','away'],
                  ['optimal', 'negative', 'optimal','low','low','low','ac','away'],
                  ['high', 'negative', 'optimal','low','low','low','ac','away'],
                  ['low', 'zero', 'optimal','low','low','low','ac','away'],
                  ['optimal', 'zero', 'optimal','low','low','low','ac','away'],
                  ['high', 'zero', 'optimal','low','low','low','ac','away'],
                  ['low', 'positive', 'optimal','low','low','low','ac','away'],
                  ['optimal', 'positive', 'optimal','low','low','low','ac','away'],
                  ['high', 'positive', 'optimal','low','low','low','ac','away'],
                  ['low', 'large', 'optimal','low','low','low','ac','away'],
                  ['optimal', 'large', 'optimal','low','low','low','ac','away'],
                  ['high', 'large', 'optimal','low','low','low','ac','away'],
                  ['low', 'negative', 'optimal','high','low','low','ac','away'],
                  ['optimal', 'negative', 'optimal','high','low','low','ac','away'],
                  ['high', 'negative', 'optimal','high','low','low','ac','away'],
                  #
                  ['low', 'zero', 'optimal','high','low','fast','ac','toward'],
                  ['optimal', 'zero', 'optimal','high','low','medium','ac','toward'],
                  ['high', 'zero', 'optimal','high','low','low','ac','away'],
                  ['low', 'positive', 'optimal','high','fast','fast','ac','toward'],
                  ['optimal', 'positive', 'optimal','high','medium','medium','ac','toward'],
                  ['high', 'positive', 'optimal','high','medium','medium','ac','toward'],
                  ['low', 'large', 'optimal','high','fast','fast','ac','toward'],
                  ['optimal', 'large', 'optimal','high','fast','fast','ac','toward'],
                  ['high', 'large', 'optimal','high','fast','fast','ac','toward'],
                  #
                  ['low', 'negative', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['optimal', 'negative', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['high', 'negative', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['low', 'zero', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['optimal', 'zero', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['high', 'zero', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['low', 'positive', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['optimal', 'positive', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['high', 'positive', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['low', 'large', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['optimal', 'large', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  ['high', 'large', 'humid', 'low', 'low', 'low', 'ac', 'away'],
                  #
                  ['low', 'negative', 'humid', 'high', 'fast', 'fast', 'de', 'toward'],
                  ['optimal', 'negative', 'humid', 'high', 'low', 'low', 'de', 'away'],
                  ['high', 'negative', 'humid', 'high', 'low', 'low', 'de', 'away'],
                  ['low', 'zero', 'humid', 'high', 'fast', 'fast', 'de', 'toward'],
                  ['optimal', 'zero', 'humid', 'high', 'medium', 'fast', 'de', 'toward'],
                  ['high', 'zero', 'humid', 'high', 'medium', 'medium', 'de', 'toward'],
                  ['low', 'positive', 'humid', 'high', 'fast', 'fast', 'ac', 'toward'],
                  ['optimal', 'positive', 'humid', 'high', 'fast', 'fast', 'ac', 'toward'],
                  ['high', 'positive', 'humid', 'high', 'medium', 'fast', 'ac', 'toward'],
                  ['low', 'large', 'humid', 'high', 'fast', 'fast', 'ac', 'toward'],
                  ['optimal', 'large', 'humid', 'high', 'fast', 'fast', 'ac', 'toward'],
                  ['high', 'large', 'humid', 'high', 'fast', 'fast', 'ac', 'toward']])

def temp(x):
    tempList=[]
    def tlow(x):
        if x<=22:
            tempList.append(1)
        elif x>22 and x<=25:
            tempList.append((25-x)/3)
        else:
            tempList.append(0)
    def toptimal(x):
        if x>=22 and x<=25:
             tempList.append((x-22)/3)
        elif x>25 and x<=28:
            tempList.append((28-x)/3)
        else:
            tempList.append(0)
    def thigh(x):
        if x>=25 and x<=28:
            tempList.append((x-25)/3)
        elif  x>28 and x<=30:
            tempList.append(1)
        else:
            tempList.append(0)
    tlow(x)
    toptimal(x)
    thigh(x)
    return tempList

def Tdifference(x):
    diffList=[]
    if x<-1 or x>3:
        raise
    def negative(x):
        if x>=-1 and x<=-0.9:
            diffList.append(1)
        elif x>-0.9 and x<=0:
            diffList.append(-0.9*x)
        else:
            diffList.append(0)
    def zero(x):
        if x>=-0.5 and x<=0:
             diffList.append(2*(x+0.5))
        elif x>0 and x<=0.5:
            diffList.append(2*(0.5-x))
        else:
            diffList.append(0)
    def positive(x):
        if x>=0 and x<=1:
            diffList.append(x)
        elif  x>1 and x<=2:
            diffList.append(2-x)
        else:
            diffList.append(0)
    def large(x):
        if x>=1 and x<=2:
            diffList.append(1-x)
        elif  x>2 and x<=3:
            diffList.append(1)
        else:
            diffList.append(0)
    negative(x)
    zero(x)
    positive(x)
    large(x)
    return diffList

def electric_volt(x):
    electricList=[]
    def Vlow(x):
        if x<=160 and x>=130:
            electricList.append(1)
        elif x>=160 and x<=180:
            electricList.append((180-x)/20)
        else:
            electricList.append(0)
    def Vregular(x):
        if x<=190 and x>=170:
             electricList.append((x-170)/20)
        elif x>190 and x<=220:
            electricList.append(1)
        else:
            electricList.append(0)

    Vlow(x)
    Vregular(x)
    return electricList

def dew_point(x):
    dewList=[]
    def Doptimal(x):
        if x<=11 and x>=10:
            dewList.append(1)
        elif x>11 and x<=14:
            dewList.append((14-x)/3)
        else:
            dewList.append(0)
    def Dhumid(x):
        if x<=15 and x>=12:
             dewList.append((x-12)/3)
        elif x>15 and x<18:
            dewList.append(1)
        else:
            dewList.append(0)

    Doptimal(x)
    Dhumid(x)
    return dewList



def calculate(temperature:[], volts:[],dew:[],difference:[]):
    temp=0
    diff=0
    d=0
    v=0
    CSlow=0
    CSmedium=0
    CShigh=0
    Fslow=0
    Fsmedium=0
    Fsfast=0
    MoAC=0
    MoDE=0
    FNaway=0
    FNtowards=0
    result=0

    for rule in rules:
        #temperature,tempDifference,dewPoint,Volt---Compressor,fanspeed,mode,finDirection

        if rule[0] == 'low':
            temp=temperature[0]
        elif rule[0] == 'optimal':
            temp=temperature[1]
        elif rule[0] == 'high':
            temp =temperature[2]

        if rule[1]== 'negative':
            diff = difference[0]
        elif rule[1] == 'zero':
            diff= difference[1]
        elif rule[1] == 'positive':
            diff = difference[2]
        elif rule[1] == 'large':
            diff = difference[3]

        if rule[2] == 'optimal':
            d = dew[0]
        elif rule[2] == 'humid':
            d = dew[1]

        if rule[3] == 'low':
            v = volts[0]
        elif rule[3] == 'high':
            v = volts[1]
        # -----------------------------------------------------------------------------------------------
        result=min(temp,diff,d,v)

        if rule[4] == 'low':
                if CSlow<result:
                    CSlow=result
        elif rule[4] == 'medium':
                if CSmedium<result:
                    CSmedium=result
        elif rule[4] == 'fast':
            if CShigh < result:
                CShigh = result

        if rule[5] == 'low':
                if Fslow<result:
                    Fslow=result
        elif rule[5] == 'medium':
            if Fsmedium < result:
                Fsmedium = result
        elif rule[5] == 'fast':
            if Fsfast < result:
                Fsfast = result


        if rule[6] == 'ac':
                if MoAC<result:
                    MoAC=result
        elif rule[6] == 'de':
            if MoDE < result:
                MoDE = result

        if rule[7] == 'away':
                if FNaway<result:
                    FNaway=result
        elif rule[7] == 'toward':
                if FNtowards<result:
                    FNtowards=result


    CSspeed=[CSlow,CSmedium,CShigh]
    FSspeed=[Fslow,Fsmedium,Fsfast]
    Mode=[MoAC,MoDE]
    FDirection=[FNaway,FNtowards]
    return {'csspeed':CSspeed,'fsspeed':FSspeed,'mode':Mode,'fdirection':FDirection}

def defuzzify(dictionary):

    CSspeed=(30*dictionary['csspeed'][0]+60*dictionary['csspeed'][1]+90*dictionary['csspeed'][2])/\
            (dictionary['csspeed'][0]+dictionary['csspeed'][1]+dictionary['csspeed'][2])
    FSspeed = (30 * dictionary['fsspeed'][0] + 60 * dictionary['fsspeed'][1] + 90 * dictionary['fsspeed'][2]) / \
              (dictionary['fsspeed'][0] + dictionary['fsspeed'][1] + dictionary['fsspeed'][2])
    Mode=dictionary['mode'][0]*1/(dictionary['mode'][0]+dictionary['mode'][1])
    FnDirection=(87.5*dictionary['fdirection'][0]+12.5*dictionary['fdirection'][1])/(dictionary['fdirection'][0]+dictionary['fdirection'][1])

    return  CSspeed,FSspeed,Mode,FnDirection


if __name__ == '__main__':
    print('Input variables- temperature=23, volts=174, dew point=13, temperature difference=0.25')
    print(f'Fuzzified input variables- temperature: {temp(23)}, volts: {electric_volt(174)},\n  dew point: {dew_point(13)}, difference of temperature: {Tdifference(0.25)}')
    fuzzified=calculate(temp(23),electric_volt(174),dew_point(13),Tdifference(0.25))
    print("------------------------------------")
    print("Fuzzified output")
    print(fuzzified.items())
    defuzy=defuzzify(fuzzified)
    print(f'predicted compressor speed {defuzy[0]}')
    print(f'predicted fan speed {defuzy[1]}')
    print(f'predicted ac value {defuzy[2]}')
    print(f'predicted fin direction {defuzy[3]}')





