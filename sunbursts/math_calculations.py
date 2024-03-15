"""
Performs math calculations based on survey and element responses.

This function retrieves data from SurveyResponse and ElementResponse instances,
performs math calculations on the data, and generates calculated values
for each participant.

Returns:
    None
"""
from .models import SurveyResponse, ElementResponse

import pandas as pd

def math_calculations():
    """
    Performs math calculations based on survey and element responses.

    Retrieves data from SurveyResponse and ElementResponse instances,
    performs math calculations on the data, and generates calculated values
    for each participant.

    Prints the calculated DataFrames for each participant.

    Returns:
        None
    """
    survey_responses = SurveyResponse.objects.all().prefetch_related('element_responses')
    print("Survey Responses:", survey_responses)
    data = []
    for survey_response in survey_responses:
        for element_response in survey_response.element_responses.all():
            data.append({
                'Element': element_response.element.name,
                'Participant': survey_response.survey,
                'Weighting': element_response.weighting,
                'Readiness': element_response.readiness,
                'Now': element_response.trendnow,
                'Needed': element_response.trendneeded,
                'Category': element_response.element.category
            })
    df = pd.DataFrame(data)

    participant_dfs = {}

    # Iterate over unique values in the 'Participant' column
    for participant in df['Participant'].unique():
        # Filter the DataFrame for the current participant
        participant_df = df[df['Participant'] == participant]
        # Store the filtered DataFrame in the dictionary
        participant_dfs[participant] = participant_df

    # Now you have separate DataFrames for each participant
    # You can perform calculations for each participant as needed
    for participant, participant_df in participant_dfs.items():
        total_votes = participant_df.groupby('Element')['Participant'].nunique()
        total_votes_column = participant_df.groupby('Element')['Participant'].nunique()
        print("total votes column", total_votes_column)

        # Normalized Vote
        range_total_votes_column = max(total_votes_column) - min(total_votes_column)
        normalized_vote = (total_votes - min(total_votes_column)) / range_total_votes_column

        # Avg Points
        avg_points = participant_df.groupby('Element')['Weighting'].sum() / total_votes

        # Normalized Points
        normalized_points = (avg_points - avg_points.min()) / (avg_points.max() - avg_points.min())

        # Avg Readiness
        avg_readiness = participant_df.groupby('Element')['Readiness'].sum() / avg_points

        # Trend Diff
        trend_diff = ((participant_df['Now'] - participant_df['Needed']).abs()).groupby(participant_df['Element']).sum() / total_votes

        # Point score
        point_score = (normalized_vote * 100) + (normalized_points * 100)

        # Need Score
        need_score = (avg_readiness * 10) + (trend_diff * 20)

        # Score
        score = point_score + need_score

        # Round the values
        normalized_vote = round(normalized_vote, 2)
        normalized_points = normalized_points.round(2)
        avg_readiness = round(avg_readiness, 2)
        trend_diff = round(trend_diff, 2)
        point_score = round(point_score, 2)
        need_score = round(need_score, 2)
        score = round(score, 2)

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

    # Print the original DataFrame for debugging
    # for participant, participant_df in participant_dfs.items():
    #     print(f"DataFrame for {participant}:")
        print(participant_df)