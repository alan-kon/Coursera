def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    df=pd.read_csv("NISPUF17.csv")
    copia=df['HAD_CPOX']
    copia2=df['P_NUMVRC']
    copias= pd.DataFrame([copia, copia2], index=['HAD_CPOX', 'P_NUMVRC'])
    copiasT=copias.T
    copiasTna=copiasT.dropna()
    copiasTna12=copiasTna[copiasTna['HAD_CPOX'] != 77]
    corr, pval=stats.pearsonr(copiasTna12["HAD_CPOX"],copiasTna12["P_NUMVRC"])
    return corr
