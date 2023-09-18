import numbers
from typing import DefaultDict

import pandas as pd

def generate(data:pd.DataFrame)-> pd.DataFrame:
    """
    Parameters:
        data: pd.DataFrame, 从教务系统导出的成绩单
    Returns:
        result: pd.DataFrame, 计算结果
    Abstract:
        生成对应的换算GPA及课程优秀率、优良率、及格率
    """

    data = data[(data.成绩 != '缓考')&(data.成绩!='IP')&(data.成绩!='W')]
    data.drop_duplicates(subset=['学号','课程号'],keep='last',inplace=True)
    data['成绩']=data['成绩'].apply(pd.to_numeric,errors='ignore')
    data['课程号'] = data['课程号'].astype(str)
    data['学号']=data['学号'].astype(str)
    data['学分']=data['学分'].apply(pd.to_numeric,errors='ignore')
    alcls=DefaultDict(int)
    pcls=DefaultDict(int)
    finecls=DefaultDict(int)
    excls=DefaultDict(int)
    npfcls=DefaultDict(int)
    realPoint=DefaultDict(float)
    sumG = DefaultDict(float)
    
    for _,lines in data.iterrows():
        point = lines['学分']
        score = lines['成绩']
        id=lines['学号']
        if type(score)!=str:
            isd = True
        else:
            isd = False


        if isd is True:
            assert isinstance(score,numbers.Number)
            if score>=85:
                excls[id]+=1
            if score>=75:
                finecls[id]+=1
            if score>=60:
                pcls[id]+=1
                sumG[id] += round(point * (4-3*(float(100-score)*float(100-score))/1600),3)
            realPoint[id] += point
            alcls[id]+=1
            npfcls[id]+=1

        else:
            assert isinstance(score,str)
            if score=='缓考' or score=='IP':
                pass
            if score=='不合格':
                alcls[id]+=1
            elif score=='合格':
                alcls[id]+=1
                pcls[id]+=1
            elif score=='A':
                realPoint[id] += point
                sumG[id] += point * 3.9
                npfcls[id]+=1
                pcls[id]+=1
                alcls[id]+=1
                finecls[id]+=1
                excls[id]+=1
            elif score=='B':
                realPoint[id] += point
                sumG[id] += point * 3.4
                npfcls[id]+=1
                pcls[id]+=1
                alcls[id]+=1
                finecls[id]+=1
            elif score=='C':
                realPoint[id] += point
                sumG[id] += point * 2.5
                npfcls[id]+=1
                pcls[id]+=1
                alcls[id]+=1
            elif score=='D':
                realPoint[id] += point
                sumG[id] += point * 1.5
                npfcls[id]+=1
                pcls[id]+=1
                alcls[id]+=1
            elif score=='F':
                realPoint[id] += point
                npfcls[id]+=1
                alcls[id]+=1
            
    Apct=DefaultDict(float)
    Ppct=DefaultDict(float)
    Bpct=DefaultDict(float)
    comGPA = DefaultDict(float)

    for key in alcls.keys():
        if npfcls[key]!=0:
            Bpct[key]=finecls[key]/npfcls[key]
            Apct[key]=excls[key]/npfcls[key]
            comGPA[key]=sumG[key]/realPoint[key]
        else:
            comGPA[key]=0
            Bpct[key]=0
            Apct[key]=0
        Ppct[key]=pcls[key]/alcls[key]

    result=pd.DataFrame({'优秀率':list(Apct.values()),'优良率':list(Bpct.values()),'及格率':list(Ppct.values()),'换算绩点':list(comGPA.values())})
    result['优秀率'] = result['优秀率'].apply(lambda x: format(x, '.3%'))
    result['优良率'] = result['优良率'].apply(lambda x: format(x, '.3%'))
    result['及格率'] = result['及格率'].apply(lambda x: format(x, '.3%'))
    result['换算绩点'] = result['换算绩点'].apply(lambda x: format(x, '.3f'))
    return result