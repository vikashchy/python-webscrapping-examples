import pandas as pd

#  Read HTML file data from internet
us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(us_states)    # ----> print all dataframe
# Read selected data from list of dataframes
df1=us_states[0][0:5][0:1]
print(df1)
newdf = df1.ix[:,0:2]    # --- > df1.ix[rows,columns]
print(newdf.columns)