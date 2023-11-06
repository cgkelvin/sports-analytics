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


coach_data = commonteamroster.CommonTeamRoster(team_id=1610612737, season=2022)
coach_data_df = coach_data.coaches.get_data_frame()
coach_name = coach_data_df[coach_data_df['COACH_TYPE'] == 'Head Coach']['COACH_NAME'][0]
coach_data_df
coach_name


from nba_api.stats.endpoints import playoffpicture

# Create an instance of the PlayoffPicture object
playoff_picture = playoffpicture.PlayoffPicture(season_id='22005')

# Call the get_data_frames method to retrieve the data frames
data = pd.DataFrame(columns=['East Wins', 'East Team'])
playoff_picture = playoffpicture.PlayoffPicture(season_id=22021)
playoff_picture_east_df = playoff_picture.east_conf_standings.get_data_frame()
playoff_picture_east_df
east_team_wins = playoff_picture_east_df['WINS']
east_team = playoff_picture_east_df['TEAM']

data_df = pd.DataFrame({
    'East Wins': east_team_wins,
    'East Team': east_team
})

data_df
data = pd.concat([data, data_df])
data


# Now, data_frames contains the data frames with the playoff picture data[]

data = []
data.append([teams, wins])
pd.DataFrame(data)


for season in range(2005, 2024):
    print('2'+f"{(season)}")


import pandas as pd
from nba_api.stats.endpoints import playoffpicture

# Initialize an empty DataFrame to store the data
playoff_picture_df = pd.DataFrame(columns=['Season', 'Team', 'Team ID', 'Wins', 'Losses', 'Win PCT', 'Clinched'])

for season in range(2005, 2024):
    playoff_picture = playoffpicture.PlayoffPicture(season_id='2' + str(season))
    
    playoff_picture_east_df = playoff_picture.east_conf_standings.get_data_frame()
    east_team_wins = playoff_picture_east_df['WINS']
    east_team_losses = playoff_picture_east_df['LOSSES']
    east_team_pct = playoff_picture_east_df['PCT']
    east_team = playoff_picture_east_df['TEAM']
    east_team_id = playoff_picture_east_df['TEAM_ID']
    east_team_clinched_playoffs = playoff_picture_east_df['CLINCHED_PLAYOFFS']
    
    east_df = pd.DataFrame({
        'Season': f"{season}-{str(season + 1)[-2:]}",
        'Team': east_team,
        'Team ID': east_team_id,
        'Wins': east_team_wins,
        'Losses': east_team_losses,
        'Win PCT': east_team_pct,
        'Clinched': east_team_clinched_playoffs
    })
    
    playoff_picture_west_df = playoff_picture.west_conf_standings.get_data_frame()
    west_team_wins = playoff_picture_west_df['WINS']
    west_team_losses = playoff_picture_west_df['LOSSES']
    west_team_pct = playoff_picture_west_df['PCT']
    west_team = playoff_picture_west_df['TEAM']
    west_team_id = playoff_picture_west_df['TEAM_ID']
    west_team_clinched_playoffs = playoff_picture_west_df['CLINCHED_PLAYOFFS']
    
    west_df = pd.DataFrame({
        'Season': f"{season}-{str(season + 1)[-2:]}",
        'Team': west_team,
        'Team ID': west_team_id,
        'Wins': west_team_wins,
        'Losses': west_team_losses,
        'Win PCT': west_team_pct,
        'Clinched Playoffs': west_team_clinched_playoffs,
        'Clinched Conference': west_team_clinched_conference,
        'Clinched '
    })
    
    # Concatenate East and West DataFrames vertically
    playoff_picture_df = pd.concat([playoff_picture_df, east_df, west_df])

# Reset index if needed
playoff_picture_df.reset_index(drop=True, inplace=True)

# Display the final DataFrame
print(playoff_picture_df)

playoff_picture_east_df = playoff_picture.get_data_frames()
data = pd.DataFrame(playoff_picture_east_df)

from nba_api.stats.endpoints import playoffpicture
WestConfPlayoffPicture_df = playoff_picture.west_conf_playoff_picture.get_data_frame()
WestConfPlayoffPicture_df['HIGH_SEED_RANK']