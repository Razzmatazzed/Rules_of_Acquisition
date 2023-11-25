#Random Rule of the Day

#Import .csv data - DONE
#Assign vector data - 1 is first rule etc. as variables? Don't have to it seems
#Define algorithm - generate random rule - DONE
#Check for date, if new day - generate new rule?

import pandas as pd
import random as rd


directory = 'https://memory-alpha.fandom.com/wiki/Rules_of_Acquisition'
df = pd.read_html(directory)[1]
rrule = rd.randrange(0,len(df))
print(df.loc[rrule][1])
