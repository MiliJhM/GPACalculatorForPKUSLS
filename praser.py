import pandas as pd

def prase(input: pd.DataFrame) -> pd.DataFrame:
    """
    Parameters: 
        input: pd.DataFrame, 从门户网站上复制的成绩单
    Returns:
        input: pd.DataFrame, 处理后的兼容格式
    Abstract:
        一共五行代码有啥可形容的
    """
    input = input.iloc[:,:5]
    input.columns=["课程号","英文名","课程类别","学分", "成绩"]
    input.dropna(axis = 0, how = "any", inplace = True)
    input = input[(1-input["课程号"].astype(str).str.endswith("课程名称")).astype(bool)]
    input.insert(0, "学号", "2147483647")
    return input