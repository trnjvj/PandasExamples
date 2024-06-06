df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[16]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

df[df.AAA <= 5]
Out[17]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50

df[df.AAA > 5]
Out[18]: 
   AAA  BBB  CCC
2    6   30  -30
3    7   40  -50






Create a list of dataframes, split using a delineation based on logic included in rows.

df = pd.DataFrame(

    data={

        "Case": ["A", "A", "A", "B", "A", "A", "B", "A", "A"],

        "Data": np.random.randn(9),

    }

)



dfs = list(

    zip(

        *df.groupby(

            (1 * (df["Case"] == "B"))

            .cumsum()

            .rolling(window=3, min_periods=1)

            .median()

        )

    )

)[-1]



dfs[0]
Out[148]: 
  Case      Data
0    A  0.276232
1    A -1.087401
2    A -0.673690
3    B  0.113648

dfs[1]
Out[149]: 
  Case      Data
4    A -1.478427
5    A  0.524988
6    B  0.404705

dfs[2]
Out[150]: 
  Case      Data
7    A  0.577046
8    A -1.715002







