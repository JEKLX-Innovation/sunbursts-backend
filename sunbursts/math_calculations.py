import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('MathData.csv')  # Replace 'MathData.csv' with the actual file path

# Extract the 'Weighting', 'Readiness', 'Now', 'Needed', and 'EntryID' columns
extracted_columns = df[['EntryID', 'Weighting', 'Readiness', 'Now', 'Needed']]

# Display the extracted columns
# print(extracted_columns)

# Get the unique EntryIDs
unique_entry_ids = df['EntryID'].unique()
votes = len(unique_entry_ids)
# print("Votes:", votes)

# Normalized Vote
# "=ARRAY_CONSTRAIN(ARRAYFORMULA((TotalVotes-MIN(TotalVotesColumn))/(MAX(TotalVotesColumn-MIN(TotalVotesColumn)))), 1, 1)"
# TotalVotes=votes
# TotalVotesColumn=total_votes
total_votes = len(df)
# print("Total Votes:", total_votes)

# Avg Points
# "=IFERROR(('Participant 1'!Weight+'Participant 2'!Weight)/TotalVotes,"")"
# element_weights = df.groupby('Element')['Weighting'].sum()
avg_points= df.groupby('Element')['Weighting'].sum()/votes
# print("Avg Points:", avg_points)


# Normalized Points
# "=IFERROR(((AvgPoints-MIN(AvgPointsColumn))/MAX(AvgPointsColumn)),"")"

avg_points_column=avg_points.sum()
# print("Avg Points Column:", avg_points_column)

normalized_points = (avg_points-(avg_points.min()))/(avg_points.max())
# print("Normalized Points:", normalized_points)


# Avg Readiness
# "=IFERROR(('Participant 1'!ReadinessValue+'Participant 2'!ReadinessValue)/$TotalVotes,"")"
readiness_value = df.groupby('Element')['Readiness'].sum()/avg_points
# print("Readiness Value:", readiness_value)

# Tred Dif
# "=IF($TotalVotes<>0,IFERROR(('Participant 1'!TrendDif+'Participant 2'!TrendDif)/$TotalVotes,0),"")"

trend_dif = ((df['Now'] - df['Needed']).abs()).groupby(df['Element']).sum() / votes
print("Trend Difference:", trend_dif)

