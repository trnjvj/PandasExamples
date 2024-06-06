df = pd.DataFrame(

    data={

        "Province": ["ON", "QC", "BC", "AL", "AL", "MN", "ON"],

        "City": [

            "Toronto",

            "Montreal",

            "Vancouver",

            "Calgary",

            "Edmonton",

            "Winnipeg",

            "Windsor",

        ],

        "Sales": [13, 6, 16, 8, 4, 3, 1],

    }

)



table = pd.pivot_table(

    df,

    values=["Sales"],

    index=["Province"],

    columns=["City"],

    aggfunc="sum",

    margins=True,

)



table.stack("City", future_stack=True)
Out[153]: 
                    Sales
Province City            
AL       Calgary      8.0
         Edmonton     4.0
         Montreal     NaN
         Toronto      NaN
         Vancouver    NaN
...                   ...
All      Toronto     13.0
         Vancouver   16.0
         Windsor      1.0
         Winnipeg     3.0
         All         51.0

[48 rows x 1 columns]

Frequency table like plyr in R

grades = [48, 99, 75, 80, 42, 80, 72, 68, 36, 78]

df = pd.DataFrame(

    {

        "ID": ["x%d" % r for r in range(10)],

        "Gender": ["F", "M", "F", "M", "F", "M", "F", "M", "M", "M"],

        "ExamYear": [

            "2007",

            "2007",

            "2007",

            "2008",

            "2008",

            "2008",

            "2008",

            "2009",

            "2009",

            "2009",

        ],

        "Class": [

            "algebra",

            "stats",

            "bio",

            "algebra",

            "algebra",

            "stats",

            "stats",

            "algebra",

            "bio",

            "bio",

        ],

        "Participated": [

            "yes",

            "yes",

            "yes",

            "yes",

            "no",

            "yes",

            "yes",

            "yes",

            "yes",

            "yes",

        ],

        "Passed": ["yes" if x > 50 else "no" for x in grades],

        "Employed": [

            True,

            True,

            True,

            False,

            False,

            False,

            False,

            True,

            True,

            False,

        ],

        "Grade": grades,

    }

)



df.groupby("ExamYear").agg(

    {

        "Participated": lambda x: x.value_counts()["yes"],

        "Passed": lambda x: sum(x == "yes"),

        "Employed": lambda x: sum(x),

        "Grade": lambda x: sum(x) / len(x),

    }

)


Out[156]: 
          Participated  Passed  Employed      Grade
ExamYear                                           
2007                 3       2         3  74.000000
2008                 3       3         0  68.500000
2009                 3       2         2  60.666667

Plot pandas DataFrame with year over year data

To create year and month cross tabulation:

df = pd.DataFrame(

    {"value": np.random.randn(36)},

    index=pd.date_range("2011-01-01", freq="ME", periods=36),

)



pd.pivot_table(

    df, index=df.index.month, columns=df.index.year, values="value", aggfunc="sum"

)


Out[158]: 
        2011      2012      2013
1  -1.039268 -0.968914  2.565646
2  -0.370647 -1.294524  1.431256
3  -1.157892  0.413738  1.340309
4  -1.344312  0.276662 -1.170299
5   0.844885 -0.472035 -0.226169
6   1.075770 -0.013960  0.410835
7  -0.109050 -0.362543  0.813850
8   1.643563 -0.006154  0.132003
9  -1.469388 -0.923061 -0.827317
10  0.357021  0.895717 -0.076467
11 -0.674600  0.805244 -1.187678
12 -1.776904 -1.206412  1.130127