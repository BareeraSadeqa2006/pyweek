import pandas as pd
df=pd.read_csv('ipl-matches.csv')
print(df)

                                # task 1:-load and inspect the data

# displaying first 3rows
print(df.head(3))

# displaying number of rows and columns
print(df.shape)

                                # task 2:- basic insights


# listing all the seasons and teams
print(df['Season'].unique())
print(df['Team1'].unique())

# matches played per season
print(df['Season'].value_counts())

# which has won the most matches?
print(df['WinningTeam'].value_counts().head(1))

                                # task 3:-Filtering data


# matches where mumbai indains has won
print(df['WinningTeam'][df['WinningTeam']=='Mumbai Indians'])

# the matches that went to super over
print(df[df['SuperOver']=='Y'])

# matches that were held at eden gardens
print(df[df['Venue']=='Eden Gardens'])


                               # task 4:-Aggregations


# checks if toss winner is match winner
print(df[df['TossWinner']==df['WinningTeam']].shape[0]/df.shape[0]*100)