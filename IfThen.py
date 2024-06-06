df.loc[df.AAA >= 5, "BBB"] = -1

df
Out[4]: 
   AAA  BBB  CCC
0    4   10  100
1    5   -1   50
2    6   -1  -30
3    7   -1  -50





An if-then with assignment to 2 columns:

df.loc[df.AAA >= 5, ["BBB", "CCC"]] = 555

df
Out[6]: 
   AAA  BBB  CCC
0    4   10  100
1    5  555  555
2    6  555  555
3    7  555  555

Add another line with different logic, to do the -else

df.loc[df.AAA < 5, ["BBB", "CCC"]] = 2000

df
Out[8]: 
   AAA   BBB   CCC
0    4  2000  2000
1    5   555   555
2    6   555   555
3    7   555   555

Or use pandas where after you’ve set up a mask

df_mask = pd.DataFrame(

    {"AAA": [True] * 4, "BBB": [False] * 4, "CCC": [True, False] * 2}

)



df.where(df_mask, -1000)
Out[10]: 
   AAA   BBB   CCC
0    4 -1000  2000
1    5 -1000 -1000
2    6 -1000   555
3    7 -1000 -1000

if-then-else using NumPy’s where()

df = pd.DataFrame(

    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

)



df
Out[12]: 
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

df["logic"] = np.where(df["AAA"] > 5, "high", "low")

df
Out[14]: 
   AAA  BBB  CCC logic
0    4   10  100   low
1    5   20   50   low
2    6   30  -30  high
3    7   40  -50  high