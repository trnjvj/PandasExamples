df = pd.DataFrame(

    np.random.randn(6, 1),

    index=pd.date_range("2013-08-01", periods=6, freq="B"),

    columns=list("A"),

)



df.loc[df.index[3], "A"] = np.nan

df
Out[102]: 
                   A
2013-08-01  0.721555
2013-08-02 -0.706771
2013-08-05 -1.039575
2013-08-06       NaN
2013-08-07 -0.424972
2013-08-08  0.567020

df.bfill()
Out[103]: 
                   A
2013-08-01  0.721555
2013-08-02 -0.706771
2013-08-05 -1.039575
2013-08-06 -0.424972
2013-08-07 -0.424972
2013-08-08  0.567020



