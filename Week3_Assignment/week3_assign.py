def answer_one():
    # YOUR CODE HERE
    energy = pd.read_excel("assets/Energy Indicators.xls", na_values = "...", header = None, skiprows = 8, skipfooter = 38, usecols = [2,3,4,5], names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea",
                                                    "United States of America": "United States",
                                                    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                    "China, Hong Kong Special Administrative Region": "Hong Kong"})
    
    energy['Country'] = energy['Country'].str.extract('(^[a-zA-Z\s]+)', expand=False).str.strip()
    #print(energy.head())
    
    #load the dataframe 
    GDP = pd.read_csv("assets/world_bank.csv", skiprows = 4)
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", 
                                            "Iran, Islamic Rep.": "Iran",
                                            "Hong Kong SAR, China": "Hong Kong"})

    SkimEn = pd.read_excel("assets/scimagojr-3.xlsx")
    #print(SkimEn.head())
    
    #merge the data 
    merge1 = pd.merge(SkimEn,energy,how = "inner", left_on = 'Country', right_on = 'Country')
    merge1 = merge1[merge1['Rank']<=15]
    
    GDP.rename(columns = {"Country Name":"Country"}, inplace = True)
    GDP = GDP.loc[:,['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','Country']]
    
    merge2 =pd.merge(merge1,GDP,how = "inner").set_index = ('Country')
    return merge2