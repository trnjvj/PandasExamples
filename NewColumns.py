df = pd.DataFrame({"AAA": [1, 2, 1, 3], "BBB": [1, 1, 2, 2], "CCC": [2, 1, 3, 1]})

df
Out[54]: 
   AAA  BBB  CCC
0    1    1    2
1    2    1    1
2    1    2    3
3    3    2    1

source_cols = df.columns  # Or some subset would work too

new_cols = [str(x) + "_cat" for x in source_cols]

categories = {1: "Alpha", 2: "Beta", 3: "Charlie"}

df[new_cols] = df[source_cols].map(categories.get)

df
Out[59]: 
   AAA  BBB  CCC  AAA_cat BBB_cat  CCC_cat
0    1    1    2    Alpha   Alpha     Beta
1    2    1    1     Beta   Alpha    Alpha
2    1    2    3    Alpha    Beta  Charlie
3    3    2    1  Charlie    Beta    Alpha

Keep other columns when using min() with groupby

df = pd.DataFrame(

    {"AAA": [1, 1, 1, 2, 2, 2, 3, 3], "BBB": [2, 1, 3, 4, 5, 1, 2, 3]}

)



df
Out[61]: 
   AAA  BBB
0    1    2
1    1    1
2    1    3
3    2    4
4    2    5
5    2    1
6    3    2
7    3    3

Method 1 : idxmin() to get the index of the minimums

df.loc[df.groupby("AAA")["BBB"].idxmin()]
Out[62]: 
   AAA  BBB
1    1    1
5    2    1
6    3    2

Method 2 : sort then take first of each

df.sort_values(by="BBB").groupby("AAA", as_index=False).first()
Out[63]: 
   AAA  BBB
0    1    1
1    2    1
2    3    2

Notice the same results, with the exception of the index.