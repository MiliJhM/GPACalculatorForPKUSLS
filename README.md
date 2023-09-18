# GPACalculator For PKU School of Life Science

## Abstract

当前生科院的成绩分两部分组成：

* 百分制成绩
* 等级制成绩

而生科院目前又有两套成绩评价系统：

* 以原百分制成绩为基础的、将等级制成绩换算为绩点的GPA评价方式
* 以等级制成绩为基础的，将百分制成绩换算为等级的三率评价方式

同时两种评价方式计算方式又不明晰，使得大家对自己的成绩分布不甚了解。本脚本帮助大家计算自己两套系统的标准成绩情况，供大家参考。

## Method

### GPA计算

当前的等级制换算情况为：
|等级| 绩点 |
|---|----|
| A | 3.9 |
| B | 3.4 |
| C | 2.5 |
| D | 1.5 |

而百分制成绩计算公式可计为
```python
round(4-3*(float(100-score)*float(100-score))/1600),3)
```

进而以学分加权求平均数即可求GPA。

### 百分制三率计算

当前的百分制换算情况为：
|分数| 等级 |
|---|----|
| 85~100 | A |
| 75~85 | B |
| 70~75 | C |
| 60~70 | D |

进而A率、AB率、合格率只需简单计数即可得到。

注意：课程三率目前**并未统计课程学分**，目前贵院教务正在协商讨论**如何将学分平滑加权至三率计算**。

## Guide

1. 首先需要**登陆门户**，从**我的成绩-本科生成绩**页面将成绩单复制到Excel；
 > 从页面开始的学期的**学期名**选择至**最后一门课程的最后一栏**，直接粘贴进空白Excel文件即可。

2. 如果(1)顺利，应该可以在Excel中得到一个完整的成绩表格。您无需处理该表格中的无用信息与格式错误。
 > 在Excel 2019以上的版本支持如上操作。如果不支持，烦请将成绩单的每一行粘贴到Excel文件中。（本来想写HTML Praser的，摆了，写个读excel得了（本来想写自动爬虫的，摆了，写个HTML Praser吧

3. 运行main.py，在弹出的文件选择窗口中选择刚才得到的Excel文件即可。

## Discussion

1. 本脚本只负责按标准方式计算成绩情况，作者不能保证该程序计算结果真实有效，请大家不要用结果跟教务对线；
2. 本脚本计算方式基于当前的成绩计算体系，不能保证该程序一直符合成绩计算实际；
3. 当前贵院采用指标+专家评审的方式评价成绩情况，因此课程成绩情况不能准确体现成绩分布。