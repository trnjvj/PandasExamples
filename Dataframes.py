df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[40]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))]
Out[41]: 
   AAA  BBB  CCC
0    4   10  100
2    6   30  -30

Use loc for label-oriented slicing and iloc positional slicing GH 2904

df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]},

    index=["foo", "bar", "boo", "kar"],

)


There are 2 explicit slicing methods, with a third general case

    Positional-oriented (Python slicing style : exclusive of end)

    Label-oriented (Non-Python slicing style : inclusive of end)

    General (Either slicing style : depends on if the slice contains labels or positions)

df.loc["bar":"kar"]  # Label
Out[43]: 
     AAA  BBB  CCC
bar    5   20   50
boo    6   30  -30
kar    7   40  -50

# Generic

df[0:3]
Out[44]: 
     AAA  BBB  CCC
foo    4   10  100
bar    5   20   50
boo    6   30  -30

df["bar":"kar"]
Out[45]: 
     AAA  BBB  CCC
bar    5   20   50
boo    6   30  -30
kar    7   40  -50

Ambiguity arises when an index consists of integers with a non-zero start or non-unit increment.

data = {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

df2 = pd.DataFrame(data=data, index=[1, 2, 3, 4])  # Note index starts at 1.

df2.iloc[1:3]  # Position-oriented
Out[48]: 
   AAA  BBB  CCC
2    5   20   50
3    6   30  -30

df2.loc[1:3]  # Label-oriented
Out[49]: 
   AAA  BBB  CCC
1    4   10  100
2    5   20   50
3    6   30  -30

Using inverse operator (~) to take the complement of a mask

df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[51]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

df[~((df.AAA <= 6) & (df.index.isin([0, 2, 4])))]
Out[52]: 
   AAA  BBB  CCC
1    5   20   50
3    7   40  -50