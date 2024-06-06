df = pd.DataFrame(

    {

        "row": [0, 1, 2],

        "One_X": [1.1, 1.1, 1.1],

        "One_Y": [1.2, 1.2, 1.2],

        "Two_X": [1.11, 1.11, 1.11],

        "Two_Y": [1.22, 1.22, 1.22],

    }

)



df
Out[65]: 
   row  One_X  One_Y  Two_X  Two_Y
0    0    1.1    1.2   1.11   1.22
1    1    1.1    1.2   1.11   1.22
2    2    1.1    1.2   1.11   1.22

# As Labelled Index

df = df.set_index("row")

df
Out[67]: 
     One_X  One_Y  Two_X  Two_Y
row                            
0      1.1    1.2   1.11   1.22
1      1.1    1.2   1.11   1.22
2      1.1    1.2   1.11   1.22

# With Hierarchical Columns

df.columns = pd.MultiIndex.from_tuples([tuple(c.split("_")) for c in df.columns])

df
Out[69]: 
     One        Two      
       X    Y     X     Y
row                      
0    1.1  1.2  1.11  1.22
1    1.1  1.2  1.11  1.22
2    1.1  1.2  1.11  1.22

# Now stack & Reset

df = df.stack(0, future_stack=True).reset_index(1)

df
Out[71]: 
    level_1     X     Y
row                    
0       One  1.10  1.20
0       Two  1.11  1.22
1       One  1.10  1.20
1       Two  1.11  1.22
2       One  1.10  1.20
2       Two  1.11  1.22

# And fix the labels (Notice the label 'level_1' got added automatically)

df.columns = ["Sample", "All_X", "All_Y"]

df
Out[73]: 
    Sample  All_X  All_Y
row                     
0      One   1.10   1.20
0      Two   1.11   1.22
1      One   1.10   1.20
1      Two   1.11   1.22
2      One   1.10   1.20
2      Two   1.11   1.22