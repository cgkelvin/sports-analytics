### This file is used to test endpoint data

import pandas as pd
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playoffpicture

# Get a list of team info
team_info = teams.get_teams()
head_coaches_data = []

# Iterate through teams and seasons
for team in team_info:
    team_id = team['id']
    team_name = team['abbreviation']
    for season in range(2005, 2024):
        coach_data = commonteamroster.CommonTeamRoster(team_id=team_id, season=season)
        coach_data_df = coach_data.coaches.get_data_frame()
        seasons = f"{season}-{str(season+1)[-2:]}"
        if not coach_data_df.empty:
            try:
                coach_name = coach_data_df[coach_data_df['COACH_TYPE'] == 'Head Coach']['COACH_NAME'].values[0]
            except IndexError:
                coach_name = 'None'
        head_coaches_data.append({
            'Team ID': team_id,
            'Season': seasons,
            'Team': team_name,
            'Coach': coach_name
        })


### testing...
# from nba_api.stats.endpoints import commonteamroster
# coach_df = commonteamroster.CommonTeamRoster(team_id=1610612761, season=2025).coaches.get_data_frame()
# coach_name = coach_df.loc[coach_df["COACH_TYPE"] == "Head Coach", 'COACH_NAME']
# coach_name

team_record_df = pd.DataFrame(columns=['Team ID', 'Season', 'Team Name', 'Wins', 'Losses', 'Win PCT'])
from nba_api.stats.endpoints import teamyearbyyearstats
for team in team_info:
    team_id = team['id']
    team_record_data = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
    team_record_data_df = team_record_data.team_stats.get_data_frame()
    team_df = pd.DataFrame({
        'Team ID': team_id,
        'Season': team_record_data_df['YEAR'],
        'Team Name': team_record_data_df['TEAM_NAME'],
        'Wins': team_record_data_df['WINS'],
        'Losses': team_record_data_df['LOSSES'],
        'Win PCT': team_record_data_df['WIN_PCT']
    })
    team_record_df = pd.concat([team_record_df, team_df])
team_record_df


coach_data = commonteamroster.CommonTeamRoster(team_id=
1610612737, season=2022)
coach_data_df = coach_data.coaches.get_data_frame()
coach_name = coach_data_df[coach_data_df['COACH_TYPE'] == 'Head Coach']['COACH_NAME'][0]
coach_data_df
coach_name


from nba_api.stats.endpoints import playoffpicture

# Create an instance of the PlayoffPicture object
playoff_picture = playoffpicture.PlayoffPicture(season_id='22005')

# Call the get_data_frames method to retrieve the data frames
data_frames = playoff_picture.east_conf_standings.get_data_frame()
teams = data_frames['TEAM']
wins = data_frames['WINS']
wins
# Now, data_frames contains the data frames with the playoff picture data[]

data = []
data.append([teams, wins])
pd.DataFrame(data)