cols = pd.MultiIndex.from_tuples(

    [(x, y) for x in ["A", "B", "C"] for y in ["O", "I"]]

)



df = pd.DataFrame(np.random.randn(2, 6), index=["n", "m"], columns=cols)

df
Out[76]: 
          A                   B                   C          
          O         I         O         I         O         I
n  0.469112 -0.282863 -1.509059 -1.135632  1.212112 -0.173215
m  0.119209 -1.044236 -0.861849 -2.104569 -0.494929  1.071804

df = df.div(df["C"], level=1)

df
Out[78]: 
          A                   B              C     
          O         I         O         I    O    I
n  0.387021  1.633022 -1.244983  6.556214  1.0  1.0
m -0.240860 -0.974279  1.741358 -1.963577  1.0  1.0
