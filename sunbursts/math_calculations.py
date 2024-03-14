from .models import SurveyResponse, ElementResponse

import pandas as pd

# Fetch survey responses and element responses from the database
survey_responses = SurveyResponse.objects.all().prefetch_related('element_responses')
data = []
for survey_response in survey_responses:
    for element_response in survey_response.element_responses.all():
        data.append({
            'Element': element_response.element.name,
            'Participant_ID': survey_response.participant.id,
            'Weighting': element_response.weighting,
            'Readiness': element_response.readiness,
            'Now': element_response.trendnow,
            'Needed': element_response.trendneeded,
            'Category': element_response.element.category
        })

# Create a DataFrame from the fetched data
df = pd.DataFrame(data)

# Perform calculations
total_votes = df.groupby('Element')['Participant_ID'].nunique()
avg_points = df.groupby('Element')['Weighting'].sum() / total_votes
avg_readiness = df.groupby('Element')['Readiness'].sum() / total_votes
trend_diff = df.groupby('Element').apply(lambda x: (x['Now'] - x['Needed']).abs().sum()) / total_votes
normalized_vote = (total_votes - total_votes.min()) / (total_votes.max() - total_votes.min())
normalized_points = (avg_points - avg_points.min()) / (avg_points.max() - avg_points.min())
point_score = (normalized_vote * 100) + (normalized_points * 100)
need_score = (avg_readiness * 10) + (trend_diff * 20)
score = point_score + need_score

# Round the calculated values
normalized_vote = normalized_vote.round(2)
normalized_points = normalized_points.round(2)
avg_readiness = avg_readiness.round(2)
trend_diff = trend_diff.round(2)
point_score = point_score.round(2)
need_score = need_score.round(2)
score = score.round(2)

# Create a DataFrame with the calculated values
calculated_data = {
    'Element': total_votes.index,
    'Total Votes': total_votes.values,
    'Avg Points': avg_points.values,
    'Avg Readiness': avg_readiness.values,
    'Trend Difference': trend_diff.values,
    'Normalized Vote': normalized_vote.values,
    'Normalized Points': normalized_points.values,
    'Point Score': point_score.values,
    'Need Score': need_score.values,
    'Score': score.values
}
calculated_df = pd.DataFrame(calculated_data)

# Use calculated_df as needed
print(calculated_df)
print(df)