df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[20]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

…and (without assignment returns a Series)

df.loc[(df["BBB"] < 25) & (df["CCC"] >= -40), "AAA"]
Out[21]: 
0    4
1    5
Name: AAA, dtype: int64

…or (without assignment returns a Series)

df.loc[(df["BBB"] > 25) | (df["CCC"] >= -40), "AAA"]
Out[22]: 
0    4
1    5
2    6
3    7
Name: AAA, dtype: int64

…or (with assignment modifies the DataFrame.)

df.loc[(df["BBB"] > 25) | (df["CCC"] >= 75), "AAA"] = 999

df
Out[24]: 
   AAA  BBB  CCC
0  999   10  100
1    5   20   50
2  999   30  -30
3  999   40  -50

Select rows with data closest to certain value using argsort

df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[26]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

aValue = 43.0

df.loc[(df.CCC - aValue).abs().argsort()]
Out[28]: 
   AAA  BBB  CCC
1    5   20   50
0    4   10  100
2    6   30  -30
3    7   40  -50

Dynamically reduce a list of criteria using a binary operators

df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[30]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

Crit1 = df.AAA <= 5.5

Crit2 = df.BBB == 10.0

Crit3 = df.CCC > -40.0

One could hard code:

AllCrit = Crit1 & Crit2 & Crit3

…Or it can be done with a list of dynamically built criteria

import functools

CritList = [Crit1, Crit2, Crit3]

AllCrit = functools.reduce(lambda x, y: x & y, CritList)

df[AllCrit]
Out[38]: 
   AAA  BBB  CCC
0    4   10  100