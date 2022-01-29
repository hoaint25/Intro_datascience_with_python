import pandas as pd
import numpy as np 
df = pd.read_csv("asset_2.csv", index_col = 0)

#Question 1 

edus = df['EDUC1']
di = {"less than high school":0,
        "high school":0,
        "more than hig school but not college":0,
        "college":0}
n = len(edus)
di['less than high school'] = np.sum(edus==1)/n
di['high school'] = np.sum(edus==2)/n
di['more than high school but not college'] = np.sum(edus==3)/n
di['college'] = np.sum(edus==4)/n
print(di)



#Question2 

#print(df['CBF_01'])
#print(df['P_NUMFLU'])

#Show all rows in column CBF and NUMFLU
new = df.loc[:, ['CBF_01','P_NUMFLU']]
#print(new)

#drop NaN value in CBF_01 columns 
cbf_01 = new[new['CBF_01'] == 1].dropna()
cbf_02 = new[new['CBF_01'] == 2].dropna()
#print(cbf_01)
#print(cbf_02)
me1 = cbf_01['P_NUMFLU'].mean()
#print(me)
me2 = cbf_02['P_NUMFLU'].mean()

print(np.mean(cbf_01['P_NUMFLU']),np.mean(cbf_02['P_NUMFLU']))
print('-----------------------------------')

#Question3

#change NaN value in P_NUMVRC by 0 
new_data = df[df['P_NUMVRC'] >=1]

cpo1_sex1 = len(new_data[(new_data['HAD_CPOX'] == 1) & (new_data['SEX'] ==1)])
cpo1_sex2 = len(new_data[(new_data['HAD_CPOX'] == 1) & (new_data['SEX'] ==2)])
cpo2_sex1 = len(new_data[(new_data['HAD_CPOX'] == 2) & (new_data['SEX'] ==1)])
cpo2_sex2 = len(new_data[(new_data['HAD_CPOX'] == 2) & (new_data['SEX'] ==2)])

cor = {"male":0, "female":0 }
cor['male'] = cpo1_sex1/cpo2_sex1
cor['female'] = cpo1_sex2/cpo2_sex2

print(cor)
print('-----------------------------------')

#Question 4: A correlation 
import scipy.stats as stats

#print(df['HAD_CPOX'].value_counts())
#print(df['P_NUMVRC'].value_counts())
new_data = df[(df['P_NUMVRC'] >=0) & (df['HAD_CPOX'] <=2)]
#print(new_data)
had_cpox = new_data['HAD_CPOX']
p_num= new_data['P_NUMVRC']

df = pd.DataFrame({"had_chickenpox_column":had_cpox,
                    "num_chickenpox_vaccine_column":p_num})

corr,pval = stats.pearsonr(df['had_chickenpox_column'],df["num_chickenpox_vaccine_column"])
print(corr)
#print(pval)
