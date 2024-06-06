df = pd.DataFrame(

    data={

        "A": [[2, 4, 8, 16], [100, 200], [10, 20, 30]],

        "B": [["a", "b", "c"], ["jj", "kk"], ["ccc"]],

    },

    index=["I", "II", "III"],

)



def SeriesFromSubList(aList):

    return pd.Series(aList)



df_orgz = pd.concat(

    {ind: row.apply(SeriesFromSubList) for ind, row in df.iterrows()}

)



df_orgz
Out[162]: 
         0     1     2     3
I   A    2     4     8  16.0
    B    a     b     c   NaN
II  A  100   200   NaN   NaN
    B   jj    kk   NaN   NaN
III A   10  20.0  30.0   NaN
    B  ccc   NaN   NaN   NaN

Rolling apply with a DataFrame returning a Series

Rolling Apply to multiple columns where function calculates a Series before a Scalar from the Series is returned

df = pd.DataFrame(

    data=np.random.randn(2000, 2) / 10000,

    index=pd.date_range("2001-01-01", periods=2000),

    columns=["A", "B"],

)



df
Out[164]: 
                   A         B
2001-01-01 -0.000144 -0.000141
2001-01-02  0.000161  0.000102
2001-01-03  0.000057  0.000088
2001-01-04 -0.000221  0.000097
2001-01-05 -0.000201 -0.000041
...              ...       ...
2006-06-19  0.000040 -0.000235
2006-06-20 -0.000123 -0.000021
2006-06-21 -0.000113  0.000114
2006-06-22  0.000136  0.000109
2006-06-23  0.000027  0.000030

[2000 rows x 2 columns]

def gm(df, const):

    v = ((((df["A"] + df["B"]) + 1).cumprod()) - 1) * const

    return v.iloc[-1]



s = pd.Series(

    {

        df.index[i]: gm(df.iloc[i: min(i + 51, len(df) - 1)], 5)

        for i in range(len(df) - 50)

    }

)



s
Out[167]: 
2001-01-01    0.000930
2001-01-02    0.002615
2001-01-03    0.001281
2001-01-04    0.001117
2001-01-05    0.002772
                ...   
2006-04-30    0.003296
2006-05-01    0.002629
2006-05-02    0.002081
2006-05-03    0.004247
2006-05-04    0.003928
Length: 1950, dtype: float64

Rolling apply with a DataFrame returning a Scalar

Rolling Apply to multiple columns where function returns a Scalar (Volume Weighted Average Price)

rng = pd.date_range(start="2014-01-01", periods=100)

df = pd.DataFrame(

    {

        "Open": np.random.randn(len(rng)),

        "Close": np.random.randn(len(rng)),

        "Volume": np.random.randint(100, 2000, len(rng)),

    },

    index=rng,

)



df
Out[170]: 
                Open     Close  Volume
2014-01-01 -1.611353 -0.492885    1219
2014-01-02 -3.000951  0.445794    1054
2014-01-03 -0.138359 -0.076081    1381
2014-01-04  0.301568  1.198259    1253
2014-01-05  0.276381 -0.669831    1728
...              ...       ...     ...
2014-04-06 -0.040338  0.937843    1188
2014-04-07  0.359661 -0.285908    1864
2014-04-08  0.060978  1.714814     941
2014-04-09  1.759055 -0.455942    1065
2014-04-10  0.138185 -1.147008    1453

[100 rows x 3 columns]

def vwap(bars):

    return (bars.Close * bars.Volume).sum() / bars.Volume.sum()



window = 5

s = pd.concat(

    [

        (pd.Series(vwap(df.iloc[i: i + window]), index=[df.index[i + window]]))

        for i in range(len(df) - window)

    ]

)



s.round(2)
Out[174]: 
2014-01-06    0.02
2014-01-07    0.11
2014-01-08    0.10
2014-01-09    0.07
2014-01-10   -0.29
              ... 
2014-04-06   -0.63
2014-04-07   -0.02
2014-04-08   -0.03
2014-04-09    0.34
2014-04-10    0.29
Length: 95, dtype: float64