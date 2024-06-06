df = pd.DataFrame(

    {

        "animal": "cat dog cat fish dog cat cat".split(),

        "size": list("SSMMMLL"),

        "weight": [8, 10, 11, 1, 20, 12, 12],

        "adult": [False] * 5 + [True] * 2,

    }

)



df
Out[105]: 
  animal size  weight  adult
0    cat    S       8  False
1    dog    S      10  False
2    cat    M      11  False
3   fish    M       1  False
4    dog    M      20  False
5    cat    L      12   True
6    cat    L      12   True

# List the size of the animals with the highest weight.

df.groupby("animal").apply(lambda subf: subf["size"][subf["weight"].idxmax()], include_groups=False)
Out[106]: 
animal
cat     L
dog     M
fish    M
dtype: object

Using get_group

gb = df.groupby("animal")

gb.get_group("cat")
Out[108]: 
  animal size  weight  adult
0    cat    S       8  False
2    cat    M      11  False
5    cat    L      12   True
6    cat    L      12   True

Apply to different items in a group

def GrowUp(x):

    avg_weight = sum(x[x["size"] == "S"].weight * 1.5)

    avg_weight += sum(x[x["size"] == "M"].weight * 1.25)

    avg_weight += sum(x[x["size"] == "L"].weight)

    avg_weight /= len(x)

    return pd.Series(["L", avg_weight, True], index=["size", "weight", "adult"])



expected_df = gb.apply(GrowUp, include_groups=False)

expected_df
Out[111]: 
       size   weight  adult
animal                     
cat       L  12.4375   True
dog       L  20.0000   True
fish      L   1.2500   True

Expanding apply

S = pd.Series([i / 100.0 for i in range(1, 11)])

def cum_ret(x, y):

    return x * (1 + y)



def red(x):

    return functools.reduce(cum_ret, x, 1.0)



S.expanding().apply(red, raw=True)
Out[115]: 
0    1.010000
1    1.030200
2    1.061106
3    1.103550
4    1.158728
5    1.228251
6    1.314229
7    1.419367
8    1.547110
9    1.701821
dtype: float64

Replacing some values with mean of the rest of a group

df = pd.DataFrame({"A": [1, 1, 2, 2], "B": [1, -1, 1, 2]})

gb = df.groupby("A")

def replace(g):

    mask = g < 0

    return g.where(~mask, g[~mask].mean())



gb.transform(replace)
Out[119]: 
   B
0  1
1  1
2  1
3  2

Sort groups by aggregated data

df = pd.DataFrame(

    {

        "code": ["foo", "bar", "baz"] * 2,

        "data": [0.16, -0.21, 0.33, 0.45, -0.59, 0.62],

        "flag": [False, True] * 3,

    }

)



code_groups = df.groupby("code")

agg_n_sort_order = code_groups[["data"]].transform("sum").sort_values(by="data")

sorted_df = df.loc[agg_n_sort_order.index]

sorted_df
Out[124]: 
  code  data   flag
1  bar -0.21   True
4  bar -0.59  False
0  foo  0.16  False
3  foo  0.45   True
2  baz  0.33  False
5  baz  0.62   True

Create multiple aggregated columns

rng = pd.date_range(start="2014-10-07", periods=10, freq="2min")

ts = pd.Series(data=list(range(10)), index=rng)

def MyCust(x):

    if len(x) > 2:

        return x.iloc[1] * 1.234

    return pd.NaT



mhc = {"Mean": "mean", "Max": "max", "Custom": MyCust}

ts.resample("5min").apply(mhc)
Out[129]: 
                     Mean  Max Custom
2014-10-07 00:00:00   1.0    2  1.234
2014-10-07 00:05:00   3.5    4    NaT
2014-10-07 00:10:00   6.0    7  7.404
2014-10-07 00:15:00   8.5    9    NaT

ts
Out[130]: 
2014-10-07 00:00:00    0
2014-10-07 00:02:00    1
2014-10-07 00:04:00    2
2014-10-07 00:06:00    3
2014-10-07 00:08:00    4
2014-10-07 00:10:00    5
2014-10-07 00:12:00    6
2014-10-07 00:14:00    7
2014-10-07 00:16:00    8
2014-10-07 00:18:00    9
Freq: 2min, dtype: int64

Create a value counts column and reassign back to the DataFrame

df = pd.DataFrame(

    {"Color": "Red Red Red Blue".split(), "Value": [100, 150, 50, 50]}

)



df
Out[132]: 
  Color  Value
0   Red    100
1   Red    150
2   Red     50
3  Blue     50

df["Counts"] = df.groupby(["Color"]).transform(len)

df
Out[134]: 
  Color  Value  Counts
0   Red    100       3
1   Red    150       3
2   Red     50       3
3  Blue     50       1

Shift groups of the values in a column based on the index

df = pd.DataFrame(

    {"line_race": [10, 10, 8, 10, 10, 8], "beyer": [99, 102, 103, 103, 88, 100]},

    index=[

        "Last Gunfighter",

        "Last Gunfighter",

        "Last Gunfighter",

        "Paynter",

        "Paynter",

        "Paynter",

    ],

)



df
Out[136]: 
                 line_race  beyer
Last Gunfighter         10     99
Last Gunfighter         10    102
Last Gunfighter          8    103
Paynter                 10    103
Paynter                 10     88
Paynter                  8    100

df["beyer_shifted"] = df.groupby(level=0)["beyer"].shift(1)

df
Out[138]: 
                 line_race  beyer  beyer_shifted
Last Gunfighter         10     99            NaN
Last Gunfighter         10    102           99.0
Last Gunfighter          8    103          102.0
Paynter                 10    103            NaN
Paynter                 10     88          103.0
Paynter                  8    100           88.0

Select row with maximum value from each group

df = pd.DataFrame(

    {

        "host": ["other", "other", "that", "this", "this"],

        "service": ["mail", "web", "mail", "mail", "web"],

        "no": [1, 2, 1, 2, 1],

    }

).set_index(["host", "service"])



mask = df.groupby(level=0).agg("idxmax")

df_count = df.loc[mask["no"]].reset_index()

df_count
Out[142]: 
    host service  no
0  other     web   2
1   that    mail   1
2   this    mail   2

Grouping like Python’s itertools.groupby

df = pd.DataFrame([0, 1, 0, 1, 1, 1, 0, 1, 1], columns=["A"])

df["A"].groupby((df["A"] != df["A"].shift()).cumsum()).groups
Out[144]: {1: [0], 2: [1], 3: [2], 4: [3, 4, 5], 5: [6], 6: [7, 8]}

df["A"].groupby((df["A"] != df["A"].shift()).cumsum()).cumsum()
Out[145]: 
0    0
1    1
2    0
3    1
4    2
5    3
6    0
7    1
8    2
Name: A, dtype: int64
