def proportion_of_education():
    import pandas as pd
    df=pd.read_csv("NISPUF17.csv")
    x=len (df[df['EDUC1'] ==1])
    y=len (df[df['EDUC1'] ==2])
    z=len (df[df['EDUC1'] ==3])
    w=len (df[df['EDUC1'] ==4])
    return {"less than high school": x/len(df),
            "high school": y/len(df),
            "more than high school but not college": z/len(df),
            "college": w/len(df)}
import pandas as pd
df=pd.read_csv("NISPUF17.csv")
x=len (df[df['EDUC1'] ==1])
y=len (df[df['EDUC1'] ==2])
z=len (df[df['EDUC1'] ==3])
w=len (df[df['EDUC1'] ==4])
