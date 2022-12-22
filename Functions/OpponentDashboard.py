
import Functions.Imports as imp
import Functions.General as general


def team_opponent_dashboard(teams_list,id_teams,season_type):
    
    nba_teams = imp.teams.get_teams()

    for index in range(0,len(nba_teams)):
        id_team = nba_teams[index]['id']
        
        if id_team not in id_teams:
            teams_list.append(team_stats_opponent(id_team,season_type=season_type))
            id_teams.append(id_team)
            print(id_team)
            
    return id_teams, teams_list


def team_stats_opponent(id_team,season_type):
    local_game = ["Home","Road",'']
    teams_list =[]
    
    for local in local_game:
        team = team_dashboard_by_opponent(id_team,season_type,local)
        teams_list.append(team)
        
        imp.time.sleep(1)
        
    df = imp.pd.concat(teams_list)
    
    return(df)


def team_dashboard_by_opponent(id_team,season_type,local_game):
    
    teams_list = []

    seasons = imp.teamdashboardbyyearoveryear.TeamDashboardByYearOverYear(team_id= id_team).get_data_frames()[1]['GROUP_VALUE']
    
    for season in seasons:
        df_season = imp.teamdashboardbyopponent.TeamDashboardByOpponent(team_id= id_team,
                                                                       location_nullable=local_game,
                                                                       season=season,
                                                                       season_type_all_star = season_type,
                                                                       per_mode_detailed="PerGame",
                                                                       pace_adjust='Y',  
                                                                       ).get_data_frames()[3]

        df_season["LOCAL"] = local_game
        df_season["TEAM_NAME"] = id_team
        df_season["SEASON"] = season
        df_season["SEASON_TYPE"] = season_type

        all_seasons= general.drop_and_rename_coloumns(df_season)

        teams_list.append(all_seasons)
        imp.time.sleep(1)
        
    df = imp.pd.concat(teams_list)

    return(df)

