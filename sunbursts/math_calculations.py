import pandas as pd
from .models import SurveyResponse

# Fetch survey responses from the database
survey_responses = SurveyResponse.objects.all()

# Check if there are survey responses in the database
if survey_responses.exists():
    # Extract data from survey responses
    response_data = [{
        'Participant_ID': response.participant.id,
        'Weighting': response.elementresponse.weighting,
        'Readiness': response.elementresponse.readiness,
        'Now': response.elementresponse.trendnow,
        'Needed': response.elementresponse.trendneeded,
        'Element': response.element.name,
        'Category': response.element.category
    } for response in survey_responses]

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(response_data)

    # Group by element for further calculations
    grouped_df = df.groupby('Element')

    # Calculate total votes per element
    total_votes = grouped_df['Participant_ID'].nunique()

    # Calculate normalized vote
    min_total_votes = total_votes.min()
    max_total_votes = total_votes.max()
    range_total_votes = max_total_votes - min_total_votes
    normalized_vote = (total_votes - min_total_votes) / range_total_votes

    # Calculate average points per element
    avg_points = grouped_df['Weighting'].sum() / total_votes

    # Calculate normalized points
    normalized_points = (avg_points - avg_points.min()) / (avg_points.max() - avg_points.min())

    # Calculate average readiness per element
    avg_readiness = grouped_df['Readiness'].sum() / total_votes

    # Calculate trend difference
    trend_diff = (grouped_df['Now'].sub(grouped_df['Needed']).abs().sum()) / total_votes

    # Calculate point score
    point_score = (normalized_vote * 100) + (normalized_points * 100)

    # Calculate need score
    need_score = (avg_readiness * 10) + (trend_diff * 20)

    # Calculate total score
    score = point_score + need_score

    # Round the calculated values
    normalized_vote = normalized_vote.round(2)
    normalized_points = normalized_points.round(2)
    avg_readiness = avg_readiness.round(2)
    trend_diff = trend_diff.round(2)
    point_score = point_score.round(2)
    need_score = need_score.round(2)
    score = score.round(2)

    # Create a DataFrame with the calculated scores
    calculated_data = {
        'Element': total_votes.index,
        'Total Votes': total_votes.values,
        'Normalized Vote': normalized_vote.values,
        'Average Points': avg_points.values,
        'Normalized Points': normalized_points.values,
        'Average Readiness': avg_readiness.values,
        'Trend Difference': trend_diff.values,
        'Point Score': point_score.values,
        'Need Score': need_score.values,
        'Total Score': score.values
    }

    calculated_df = pd.DataFrame(calculated_data)

    # Display the calculated DataFrame
    print(calculated_df)

else:
    print("No survey responses found in the database.")
