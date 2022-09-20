import pandas as pd


df = pd.read_csv('MergeBP_complete.csv')


newdf=df.loc[
            (df['AGE'].isin(range(12,18,1)))
            &(df['BMI']>29)
            &(df['SBP'] <130)
            &(df['DBP'] > 80)
            &(df['FBS']>110)
           
             
            ]
newdf