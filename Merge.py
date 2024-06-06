rng = pd.date_range("2000-01-01", periods=6)

df1 = pd.DataFrame(np.random.randn(6, 3), index=rng, columns=["A", "B", "C"])

df2 = df1.copy()

Depending on df construction, ignore_index may be needed

df = pd.concat([df1, df2], ignore_index=True)

df
Out[181]: 
           A         B         C
0  -0.870117 -0.479265 -0.790855
1   0.144817  1.726395 -0.464535
2  -0.821906  1.597605  0.187307
3  -0.128342 -1.511638 -0.289858
4   0.399194 -1.430030 -0.639760
5   1.115116 -2.012600  1.810662
6  -0.870117 -0.479265 -0.790855
7   0.144817  1.726395 -0.464535
8  -0.821906  1.597605  0.187307
9  -0.128342 -1.511638 -0.289858
10  0.399194 -1.430030 -0.639760
11  1.115116 -2.012600  1.810662

Self Join of a DataFrame GH 2996

df = pd.DataFrame(

    data={

        "Area": ["A"] * 5 + ["C"] * 2,

        "Bins": [110] * 2 + [160] * 3 + [40] * 2,

        "Test_0": [0, 1, 0, 1, 2, 0, 1],

        "Data": np.random.randn(7),

    }

)



df
Out[183]: 
  Area  Bins  Test_0      Data
0    A   110       0 -0.433937
1    A   110       1 -0.160552
2    A   160       0  0.744434
3    A   160       1  1.754213
4    A   160       2  0.000850
5    C    40       0  0.342243
6    C    40       1  1.070599

df["Test_1"] = df["Test_0"] - 1

pd.merge(

    df,

    df,

    left_on=["Bins", "Area", "Test_0"],

    right_on=["Bins", "Area", "Test_1"],

    suffixes=("_L", "_R"),

)


Out[185]: 
  Area  Bins  Test_0_L    Data_L  Test_1_L  Test_0_R    Data_R  Test_1_R
0    A   110         0 -0.433937        -1         1 -0.160552         0
1    A   160         0  0.744434        -1         1  1.754213         0
2    A   160         1  1.754213         0         2  0.000850         1
3    C    40         0  0.342243        -1         1  1.070599         0

