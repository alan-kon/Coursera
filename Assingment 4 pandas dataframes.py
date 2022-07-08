q1="""In this assignment you must read in a file of metropolitan regions and associated sports teams from assets/wikipedia_data.html and answer some questions about each metropolitan region. Each of these regions may have one or more teams from the "Big 4": NFL (football, in assets/nfl.csv), MLB (baseball, in assets/mlb.csv), NBA (basketball, in assets/nba.csv or NHL (hockey, in assets/nhl.csv). Please keep in mind that all questions are from the perspective of the metropolitan region, and that this file is the "source of authority" for the location of a given sports team. Thus teams which are commonly known by a different area (e.g. "Oakland Raiders") need to be mapped into the metropolitan region given (e.g. San Francisco Bay Area). This will require some human data understanding outside of the data you've been given (e.g. you will have to hand-code some names, and might need to google to find out where teams are)!

For each sport I would like you to answer the question: what is the win/loss ratio's correlation with the population of the city it is in? Win/Loss ratio refers to the number of wins over the number of wins plus the number of losses. Remember that to calculate the correlation with pearsonr, so you are going to send in two ordered lists of values, the populations from the wikipedia_data.html file and the win/loss ratio for a given sport in the same order. Average the win/loss ratios for those cities which have multiple teams of a single sport. Each sport is worth an equal amount in this assignment (20%*4=80%) of the grade for this assignment. You should only use data from year 2018 for your analysis -- this is important!

Notes
Do not include data about the MLS or CFL in any of the work you are doing, we're only interested in the Big 4 in this assignment.
I highly suggest that you first tackle the four correlation questions in order, as they are all similar and worth the majority of grades for this assignment. This is by design!
It's fair game to talk with peers about high level strategy as well as the relationship between metropolitan areas and sports teams. However, do not post code solving aspects of the assignment (including such as dictionaries mapping areas to teams, or regexes which will clean up names).
There may be more teams than the assert statements test, remember to collapse multiple teams in one city into a single value!
Question 1
For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NHL using 2018 data."""



def nhl_correlation(): 
    nhl_df=pd.read_csv("assets/nhl.csv")
    cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    nhl_df=nhl_df.iloc[:,[0,2,3,-2]]
    nhl_df=nhl_df[nhl_df['year']==2018]
    nhl_df=nhl_df.replace("Atlantic Division", np.NaN)
    nhl_df=nhl_df.replace("Metropolitan Division", np.NaN)
    nhl_df=nhl_df.replace("Central Division", np.NaN)
    nhl_df=nhl_df.replace("Pacific Division", np.NaN)
    nhl_df=nhl_df.dropna()
    nhl_df=nhl_df.rename(columns={'team': 'NHL'})
    nhl_df.drop("year", inplace=True, axis=1)
    nhl_df['NHL']=nhl_df['NHL'].str.replace("*", "")
    nhl_df['NHL']=nhl_df['NHL'].str.replace(".", " ")
    nhl_df['W'][17]=113
    nhl_df['L'][17]=105
    nhl_df['W'][30]=89
    nhl_df['L'][30]=54
    nhl_df=nhl_df.drop(14)
    nhl_df=nhl_df.drop(16)
    nhl_df=nhl_df.drop(28)
    nhl_df['NHL']=nhl_df['NHL'].str.replace("[\w]*\s", "")
    cities=cities.iloc[:-1,[0,1,5]]
    cities=cities.replace("—", np.NaN)
    cities=cities.dropna()
    cities['NHL']=cities['NHL'].str.replace("[\w]*\s[\d]*", "")
    cities['NHL']=cities['NHL'].str.replace("\[]", "")
    cities=cities.replace("", np.NaN)
    cities=cities.dropna()
    cities['NHL'][0]='Rangers'
    cities['NHL'][1]='Kings'
    junta=pd.merge(cities, nhl_df, how='left', on="NHL")
    population_by_region=junta['Population (2016 est.)[8]'].array
    for i in range (28):
        population_by_region[i]=float(population_by_region[i])
    win=junta['W'].array
    lost=junta['L'].array
    win_loss_by_region = []
    for i in range(len(win)):
        ratio=float(win[i])/(float(win[i])+float(lost[i]))
        win_loss_by_region.append(ratio)

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
    
    x,y=stats.pearsonr(population_by_region, win_loss_by_region)
    return x
