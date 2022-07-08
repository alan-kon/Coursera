def average_influenza_doses():
    import pandas as pd
    df=pd.read_csv("NISPUF17.csv")
    copy_df = df.copy()
    copy_df = copy_df[(copy_df['CBF_01']==1)]
    copy_df2 = df.copy()
    copy_df2 = copy_df2[(copy_df2['CBF_01']==2)]
    x=copy_df["P_NUMFLU"]
    y=copy_df2["P_NUMFLU"]
    w=x.dropna()
    q=y.dropna()
    return (w.mean(), q.mean())



import pandas as pd
df=pd.read_csv("NISPUF17.csv")
copy_df = df.copy()
copy_df = copy_df[(copy_df['CBF_01']==1)]
copy_df2 = df.copy()
copy_df2 = copy_df2[(copy_df2['CBF_01']==2)]
x=copy_df["P_NUMFLU"]
y=copy_df2["P_NUMFLU"]
w=x.dropna()
q=y.dropna()
print(w.mean(), q.mean())
