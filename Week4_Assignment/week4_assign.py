from audioop import lin2ulaw
from cmath import log10
from math import log1p
from pstats import Stats
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

#Question1: calculate the win/loss ratio's correlation with the population of the city it is in for the NHL using 2018 data.
def nhl_correlation():
    nhl_df = pd.read_csv('nhl.csv')
    cities=pd.read_html("wikipedia_data.html")[1]
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    cities = cities.iloc[:-1,[0,3,5,6,7,8]]
    cities = cities.reset_index(drop=True)
        #drop column have 'Division in column name' in nfl_df
    nhl_df = nhl_df.drop([0,9,18,26],axis=0) #0 for rows and 1 for columns
    cities = cities.drop([14,15,18,19,20,21,23,24,25,27,28,32,33,38,40,41,42,44,45,46], axis=0)

    #delete [] in DHL columns in citties
    l = []
    for i in cities['NHL']:
        i = i.split('[')
        l.append(i[0])
    cities['NHL'] = l
    #delete * in team column in nhl_df
    li = []
    for i in nhl_df['team']:
        i = re.findall("[^*]+", i)
        li.append(i[0])
    nhl_df['team'] = li
    nhl_df = nhl_df.head(31)

    nhl_df['team_ville'] = nhl_df['team']
    nhl_df['team_ville'] = nhl_df['team_ville'].map({'Tampa Bay Lightning':'Tampa Bay Area',
        'Boston Bruins':'Boston',
        'Toronto Maple Leafs':'Toronto',
        'Florida Panthers':'Miami–Fort Lauderdale',
        'Detroit Red Wings':'Detroit',
        'Montreal Canadiens':'Montreal',
        'Ottawa Senators':'Ottawa',
        'Buffalo Sabres':'Buffalo',
        'Washington Capitals':'Washington, D.C.',
        'Pittsburgh Penguins':'Pittsburgh',
        'Philadelphia Flyers':'Philadelphia',
        'Columbus Blue Jackets':'Columbus',
        'New Jersey Devils':'New York City',
        'Carolina Hurricanes':'Raleigh',
        'New York Islanders':'New York City',
        'New York Rangers':'New York City',
        'Nashville Predators':'Nashville',
        'Winnipeg Jets':'Winnipeg',
        'Minnesota Wild':'Minneapolis–Saint Paul',
        'Colorado Avalanche':'Denver',
        'St. Louis Blues':'St. Louis',
        'Dallas Stars':'Dallas–Fort Worth',
        'Chicago Blackhawks':'Chicago',
        'Vegas Golden Knights':'Las Vegas',
        'Anaheim Ducks':'Los Angeles',
        'San Jose Sharks':'San Francisco Bay Area',
        'Los Angeles Kings':'Los Angeles',
        'Calgary Flames':'Calgary',
        'Edmonton Oilers':'Edmonton',
        'Vancouver Canucks':'Vancouver',
        'Arizona Coyotes':'Phoenix'})
    df =pd.merge(nhl_df,cities, left_on= "team_ville", right_on= "Metropolitan area")
    #print(df.head(5))
    df['w'] = pd.to_numeric(df['W'])
    df['L'] = pd.to_numeric(df['L'])
    df['Population (2016 est.)[8]'] = pd.to_numeric(df['Population (2016 est.)[8]'])
    he = ['team','W','L','Metropolitan area','Population (2016 est.)[8]']
    df = df[he]
    df['W'] = df['W'].astype(int)
    df['W'] = df['W'].astype(int)
    df['W/L'] = df['W']/(df['L']+df['W'])

    df = df.groupby('Metropolitan area').mean().reset_index()

    population_by_region = df['Population (2016 est.)[8]'] # pass in metropolitan area population from cities
    win_loss_by_region = df['W/L'] # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]

    #assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    #assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
        
    #return stats.pearsonr(population_by_region, win_loss_by_region)[0]
    return df 
#Question2: calculate the win/loss ratio's correlation with the population of the city it is in for the NBA using 2018 data.
def nba_correlation():
    nba_df =pd.read_csv('nba.csv')
    cities=pd.read_html("wikipedia_data.html")[1]
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    cities=cities.iloc[:-1,[0,3,5,6,7,8],]
    cities = cities.reset_index(drop = True)
    #print(cities['NBA'])
    cities = cities.drop([16,17,19,20,21,22,23,26,29,30,31,34,35,36,37,39,40,43,44,47,48,49,50],axis=0)

    #remove * and in TEAM column in nba_df
    l1 = []
    for i in nba_df['team']:
        i=i.split('*')
        l1.append(i[0])
    nba_df['team'] = l1
    #remove () and in TEAM column in nba_df
    l2 = []
    for i in nba_df['team']:
        i = i.split('(')
        l2.append(i[0])
    nba_df['team'] = l2
    #remove whitespace before team name in TEAM column in nba_df
    l3 = []
    for i in nba_df['team']:
        i=i.rstrip()
        l3.append(i)
    nba_df['team'] = l3

    nba_df = nba_df.head(30)
    nba_df['team'] = nba_df['team'].map({'Toronto Raptors':'Toronto',
        'Boston Celtics':'Boston',
        'Philadelphia 76ers':'Philadelphia',
        'Cleveland Cavaliers':'Cleveland',
        'Indiana Pacers':'Indianapolis',
        'Miami Heat':'Miami–Fort Lauderdale',
        'Milwaukee Bucks':'Milwaukee',
        'Washington Wizards':'Washington, D.C.',
        'Detroit Pistons':'Detroit',
        'Charlotte Hornets':'Charlotte',
        'New York Knicks':'New York City',
        'Brooklyn Nets':'New York City',
        'Chicago Bulls':'Chicago',
        'Orlando Magic':'Orlando',
        'Atlanta Hawks':'Atlanta',
        'Houston Rockets':'Houston',
        'Golden State Warriors':'San Francisco Bay Area',
        'Portland Trail Blazers':'Portland',
        'Oklahoma City Thunder':'Oklahoma City',
        'Utah Jazz':'Salt Lake City',
        'New Orleans Pelicans':'New Orleans',
        'San Antonio Spurs':'San Antonio',
        'Minnesota Timberwolves':'Minneapolis–Saint Paul',
        'Denver Nuggets':'Denver',
        'Los Angeles Clippers':'Los Angeles',
        'Los Angeles Lakers':'Los Angeles',
        'Sacramento Kings':'Sacramento',
        'Dallas Mavericks':'Dallas–Fort Worth',
        'Memphis Grizzlies':'Memphis',
        'Phoenix Suns':'Phoenix'})

    df2 = pd.merge(nba_df,cities, left_on= "team", right_on= "Metropolitan area")
    df2['W/L%'] = pd.to_numeric(df2['W/L%'])
    df2['W'] = pd.to_numeric(df2['W'])
    df2['L'] = pd.to_numeric(df2['L'])
    df2['Population (2016 est.)[8]'] = pd.to_numeric(df2['Population (2016 est.)[8]'])
    he = ['team','W','L','W/L%','Metropolitan area','Population (2016 est.)[8]']
    df2 = df2[he]
    df2['W/L'] = df2['W']/(df2['L']+df2['W'])
    df2.rename(columns = {'Population (2016 est.)[8]':'Population'},inplace = True)
    df2 = df2.groupby('Metropolitan area').mean().reset_index()
    population_by_region = df2['Population'] # pass in metropolitan area population from cities
    win_loss_by_region = df2['W/L'] # pass in win/loss ratio from nba_df in the same order as cities["Metropolitan area"]

    #assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    #assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"
    return df2
    #return (stats.pearsonr(population_by_region, win_loss_by_region)[0])
#Question 3: calculate the win/loss ratio's correlation with the population of the city it is in for the MLB using 2018 data.
def mlb_correlation():
    # YOUR CODE HERE
    #raise NotImplementedError()

    mlb_df=pd.read_csv("mlb.csv")
    cities=pd.read_html("wikipedia_data.html")[1]
    cities = cities.iloc[:-1,[0,3,5,6,7,8]]
    cities = cities.reset_index(drop=True)

    cities = cities.drop([24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50],axis=0)
    cities = cities.reset_index(drop=True)
    mlb_df = mlb_df.head(30)
    
    mlb_df['team_ville'] = mlb_df['team']
    mlb_df['team_ville'] = mlb_df['team_ville'].map({'Boston Red Sox':'Boston',
     'New York Yankees':'New York City',
     'Tampa Bay Rays':'Tampa Bay Area',
     'Toronto Blue Jays':'Toronto',
     'Baltimore Orioles':'Baltimore',
     'Cleveland Indians':'Cleveland',
     'Minnesota Twins':'Minneapolis–Saint Paul',
     'Detroit Tigers':'Detroit',
     'Chicago White Sox':'Chicago',
     'Kansas City Royals':'Kansas City',
     'Houston Astros':'Houston',
     'Oakland Athletics':'San Francisco Bay Area',
     'Seattle Mariners':'Seattle',
     'Los Angeles Angels':'Los Angeles',
     'Texas Rangers':'Dallas–Fort Worth',
     'Atlanta Braves':'Atlanta',
     'Washington Nationals':'Washington, D.C.',
     'Philadelphia Phillies':'Philadelphia',
     'New York Mets':'New York City',
     'Miami Marlins':'Miami–Fort Lauderdale',
     'Milwaukee Brewers':'Milwaukee',
     'Chicago Cubs':'Chicago',
     'St. Louis Cardinals':'St. Louis',
     'Pittsburgh Pirates':'Pittsburgh',
     'Cincinnati Reds':'Cincinnati',
     'Los Angeles Dodgers':'Los Angeles',
     'Colorado Rockies':'Denver',
     'Arizona Diamondbacks':'Phoenix',
     'San Francisco Giants':'San Francisco Bay Area',
     'San Diego Padres':'San Diego'})
    
    df3 = pd.merge(mlb_df,cities, left_on= "team_ville", right_on= "Metropolitan area")

    df3['W'] = pd.to_numeric(df3['W'])
    df3['L'] = pd.to_numeric(df3['L'])
    df3['Population (2016 est.)[8]'] = pd.to_numeric(df3['Population (2016 est.)[8]'])
    he = ['team','W','L','Metropolitan area','Population (2016 est.)[8]']
    df3 = df3[he]
    df3.rename(columns = {'Population (2016 est.)[8]':'Population'}, inplace = True)
    df3['W/L'] = df3['W']/(df3['L']+df3['W'])
    df3 = df3.groupby('Metropolitan area').mean().reset_index()
    
    
    population_by_region = df3['Population'] # pass in metropolitan area population from cities
    win_loss_by_region = df3['W/L'] # pass in win/loss ratio from mlb_df in the same order as cities["Metropolitan area"]

    return df3
    # assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    # assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    # return stats.pearsonr(population_by_region, win_loss_by_region)[0]
#Question 4:  calculate the win/loss ratio's correlation with the population of the city it is in for the NFL using 2018 data.
#def nfl_correlation(): 
def nfl_correlation():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)


    nfl_df=pd.read_csv("nfl.csv")
    cities=pd.read_html("wikipedia_data.html")[1]
    cities = cities.iloc[:-1,[0,3,5,6,7,8]]
    cities = cities.reset_index(drop=True)
    cities = cities.drop([13,22,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50],axis=0)
    cities = cities.reset_index(drop=True)

    nfl_df = nfl_df.drop([0,5,10,15,20,25,30,35],axis =0)
    nfl_df = nfl_df[nfl_df['year'] == 2018]

    l1 = []
    for i in nfl_df['team']:
            #i=i.rstrip()
        i=i.split('*')
        l1.append(i[0])
    nfl_df['team'] = l1
        
    l2 = []
    for i in nfl_df['team']:
        i=i.split('+')
        l2.append(i[0])
    nfl_df['team'] = l2

    nfl_df['team'] = nfl_df['team'].map({'New England Patriots':'Boston',
        'Miami Dolphins':'Miami–Fort Lauderdale',
        'Buffalo Bills':'Buffalo',
        'New York Jets':'New York City',
        'Baltimore Ravens':'Baltimore',
        'Pittsburgh Steelers':'Pittsburgh',
        'Cleveland Browns':'Cleveland',
        'Cincinnati Bengals':'Cincinnati',
        'Houston Texans':'Houston',
        'Indianapolis Colts':'Indianapolis',
        'Tennessee Titans':'Nashville',
        'Jacksonville Jaguars':'Jacksonville',
        'Kansas City Chiefs':'Kansas City',
        'Los Angeles Chargers':'Los Angeles',
        'Denver Broncos':'Denver',
        'Oakland Raiders':'San Francisco Bay Area',
        'Dallas Cowboys':'Dallas–Fort Worth',
        'Philadelphia Eagles':'Philadelphia',
        'Washington Redskins':'Washington, D.C.',
        'New York Giants':'New York City',
        'Chicago Bears':'Chicago',
        'Minnesota Vikings':'Minneapolis–Saint Paul',
        'Green Bay Packers':'Green Bay',
        'Detroit Lions':'Detroit',
        'New Orleans Saints':'New Orleans',
        'Carolina Panthers':'Charlotte',
        'Atlanta Falcons':'Atlanta',
        'Tampa Bay Buccaneers':'Tampa Bay Area',
        'Los Angeles Rams':'Los Angeles',
        'Seattle Seahawks':'Seattle',
        'San Francisco 49ers':'San Francisco Bay Area',
        'Arizona Cardinals':'Phoenix'}) 

    df4 = pd.merge(nfl_df,cities, left_on= "team", right_on= "Metropolitan area")
    df4['W'] = pd.to_numeric(df4['W'])
    df4['L'] = pd.to_numeric(df4['L'])
    df4['Population (2016 est.)[8]'] = pd.to_numeric(df4['Population (2016 est.)[8]'])
    he = ['team','W','L','Metropolitan area','Population (2016 est.)[8]']
    df4 = df4[he]
    df4.rename(columns = {'Population (2016 est.)[8]':'Population'}, inplace = True)
    df4['W/L'] = df4['W']/(df4['L']+df4['W'])
    df4 = df4.groupby('Metropolitan area').mean().reset_index()
    
    population_by_region = df4['Population'] # pass in metropolitan area population from cities
    win_loss_by_region = df4['W/L'] # pass in win/loss ratio from nfl_df in the same order as cities["Metropolitan area"]

    return df4
    # assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    # assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    # return stats.pearsonr(population_by_region, win_loss_by_region)[0]
#Question 5: 
def sports_team_performance():
    nhl = nhl_correlation()
    nba = nba_correlation()
    mlb = mlb_correlation()
    nfl = nfl_correlation()

    nba_nfl = pd.merge(nba,nfl, on='Metropolitan area')
    pval_nba_nfl = stats.ttest_rel(nba_nfl['W/L_x'],nba_nfl['W/L_y'])[1]
    nba_nhl = pd.merge(nba,nhl, on='Metropolitan area')
    pval_nba_nhl = stats.ttest_rel(nba_nhl['W/L_x'],nba_nhl['W/L_y'])[1]
    mlb_nfl = pd.merge(mlb,nfl, on='Metropolitan area')
    pval_mlb_nfl = stats.ttest_rel(mlb_nfl['W/L_x'],mlb_nfl['W/L_y'])[1]
    mlb_nhl = pd.merge(mlb,nhl, on='Metropolitan area')
    pval_mlb_nhl = stats.ttest_rel(mlb_nhl['W/L_x'],mlb_nhl['W/L_y'])[1]
    mlb_nba = pd.merge(mlb,nba, on='Metropolitan area')
    pval_mlb_nba = stats.ttest_rel(mlb_nba['W/L_x'],mlb_nba['W/L_y'])[1]
    nhl_nfl = pd.merge(nhl,nfl, on='Metropolitan area')
    pval_nhl_nfl = stats.ttest_rel(nhl_nfl['W/L_x'],nhl_nfl['W/L_y'])[1]

    pv = {'NFL': {"NFL": np.nan, 'NBA': pval_nba_nfl, 'NHL': pval_nhl_nfl, 'MLB': pval_mlb_nfl},
       'NBA': {"NFL": pval_nba_nfl, 'NBA': np.nan, 'NHL': pval_nba_nhl, 'MLB': pval_mlb_nba},
       'NHL': {"NFL": pval_nhl_nfl, 'NBA': pval_nba_nhl, 'NHL': np.nan, 'MLB': pval_mlb_nhl},
       'MLB': {"NFL": pval_mlb_nfl, 'NBA': pval_mlb_nba, 'NHL': pval_mlb_nhl, 'MLB': np.nan}
      }
    p_values = pd.DataFrame(pv)
    
    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    return p_values