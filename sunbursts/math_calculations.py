import pandas as pd
from .models import SurveyResponse


# Load the CSV file into a DataFrame
survey_responses = SurveyResponse.objects.all()
# df = pd.read_csv('MathData.csv') 
# df = pd.DataFrame(list(survey_responses.values()))
# print(df)
response_data = [{'Participant_ID': response.participant.id,
                  'Weighting': response.elementresponse.weighting_input,
                  'Readiness': response.elementresponse.readiness_input,
                  'Now': response.elementresponse.trend_now,
                  'Needed': response.elementresponse.trend_needed,
                  'Element': response.element.name,
                  'Category': response.element.category} 
                 for response in survey_responses]

# Create a DataFrame from the fetched data
df = pd.DataFrame(response_data)
# Extract the 'Weighting', 'Readiness', 'Now', 'Needed', and 'EntryID' columns
extracted_columns = df[['Participant_ID', 'Weighting', 'Readiness', 'Now', 'Needed','Element','Category']]

# Display the extracted columns
# print(extracted_columns)

# Get the unique EntryIDs
# unique_participant_ids = df['Participant_ID'].unique()

# total votes per element
total_votes = df.groupby('Element')['Participant_ID'].nunique()
print("Total Votes:", total_votes)

# Normalized Vote
# "=ARRAY_CONSTRAIN(ARRAYFORMULA((TotalVotes-MIN(TotalVotesColumn))/(MAX(TotalVotesColumn-MIN(TotalVotesColumn)))), 1, 1)"
# TotalVotes=votes
# TotalVotesColumn=total_votes
total_votes_column = df.groupby('Element')['Participant_ID'].nunique()
print("Total Votes Column:", total_votes_column)
# division by zero error
# normalized_vote = (total_votes - min(total_votes_column)) / (max(total_votes_column) - min(total_votes_column))
range_total_votes_column = max(total_votes_column) - min(total_votes_column)

# if range_total_votes_column == 0:
#     normalized_vote = 1
# else:
#     # Calculate the normalized vote
normalized_vote = (total_votes - min(total_votes_column)) / range_total_votes_column

# Print the normalized vote
print("Normalized Vote:", normalized_vote)

# Avg Points
# "=IFERROR(('Participant 1'!Weight+'Participant 2'!Weight)/TotalVotes,"")"
# element_weights = df.groupby('Element')['Weighting'].sum()
avg_points= df.groupby('Element')['Weighting'].sum()/total_votes
# print("Avg Points:", avg_points)


# Normalized Points
# "=IFERROR(((AvgPoints-MIN(AvgPointsColumn))/MAX(AvgPointsColumn)),"")"
avg_points_column=avg_points.sum()
# print("Avg Points Column:", avg_points_column)
normalized_points = (avg_points-(avg_points.min()))/(avg_points.max())
print("Normalized Points:", normalized_points)


# Avg Readiness
# "=IFERROR(('Participant 1'!ReadinessValue+'Participant 2'!ReadinessValue)/$TotalVotes,"")"
avg_readiness = df.groupby('Element')['Readiness'].sum()/avg_points
# print("Avg Readiness:", avg_readiness)

# Tred Diff
# "=IF($TotalVotes<>0,IFERROR(('Participant 1'!TrendDif+'Participant 2'!TrendDif)/$TotalVotes,0),"")"

trend_diff = ((df['Now'] - df['Needed']).abs()).groupby(df['Element']).sum() / total_votes
# print("Trend Difference:", trend_diff)

# Point score
# "=IFERROR(NormalizedVote*100+NormalizedPoints*100,"")"

point_score=(normalized_vote*100)+(normalized_points*100)
# print("Point Score:", point_score)
# df['Point Score'] = point_score

# Need Score
#"=IFERROR(AvgReadiness*10+TrendDif*20,"")"
need_score=(avg_readiness*10)+(trend_diff*20)
# print("Need Score:", need_score)
# df['Need Score'] = need_score


# Score
# "=IF(PointScore<>"",PointScore+NeedScore,"")"
score=point_score+need_score
# print("Score:", score)
# df['Score'] = score

normalized_vote = round(normalized_vote, 2)

normalized_points = normalized_points.round(2)

avg_readiness = round(avg_readiness, 2)

trend_diff = round(trend_diff, 2)

point_score = round(point_score, 2)

need_score = round(need_score, 2)

score = round(score, 2)

# print("Normalized Vote:", normalized_vote)
# print("Normalized Points:", normalized_points)
# print("Avg Readiness:", avg_readiness)
# print("Trend Difference:", trend_diff)
# print("Point Score:", point_score)
# print("Need Score:", need_score)
# print("Score:", score)


# new_df = pd.DataFrame({
#     'Category': df['Category'],
#     'Element': df['Element'],
#     'Score': score,
#     'Need Score': need_score,
#     'Point Score': point_score
# }, index=df.index) 

# new_df = new_df.drop_duplicates()

# print(new_df)

data = []
for cat, elem, scr, nscore, pscore in zip(df['Category'], df['Element'], score, need_score, point_score):
    data.append({'Category': cat, 'Element': elem, 'Point Score': pscore, 'Need Score': nscore, 'Score': scr})

new_df = pd.DataFrame(data)

new_df = new_df.drop_duplicates()



# print(new_df)





