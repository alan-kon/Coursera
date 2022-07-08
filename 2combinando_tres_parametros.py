def chickenpox_by_sex():
    import pandas as pd
    df=pd.read_csv("NISPUF17.csv")
    copy_df = df.copy()
    copy_df = copy_df[(copy_df['P_NUMVRC']>0)]
    m=copy_df[(copy_df['SEX']==1)]
    f=copy_df[(copy_df['SEX']==2)]
    w=m[(m['HAD_CPOX']==1)]
    z=m[(m['HAD_CPOX']==2)]
    a=f[(f['HAD_CPOX']==1)]
    b=f[(f['HAD_CPOX']==2)]
    return {"male":len(w)/len(z),
    "female":len(a)/len(b)}

#HAD_CPOX==1 e P_NUMVRC >0 e SEX==1/HAD_CPOX==2 e P_NUMVRC >0 e SEX==1
#HAD_CPOX==1 e P_NUMVRC >0 e SEX==2/HAD_CPOX==2 e P_NUMVRC >0 e SEX==2
import pandas as pd
df=pd.read_csv("NISPUF17.csv")
copy_df = df.copy()
copy_df = copy_df[(copy_df['P_NUMVRC']>0)]
m=copy_df[(copy_df['SEX']==1)]
f=copy_df[(copy_df['SEX']==2)]
w=m[(m['HAD_CPOX']==1)]
z=m[(m['HAD_CPOX']==2)]
a=f[(f['HAD_CPOX']==1)]
b=f[(f['HAD_CPOX']==2)]

