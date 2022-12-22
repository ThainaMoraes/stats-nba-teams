import Functions.Imports as imp
import Functions.General as general


def team_dashboard(teams_list,id_teams,season_type):
    
    nba_teams = imp.teams.get_teams()
    
    for index in range(0,len(nba_teams)):
        id_team = nba_teams[index]['id']
        if id_team not in id_teams:
            teams_list.append(team_stats(id_team,season_type=season_type))
            id_teams.append(id_team)
            print(id_team)
            
    return id_teams, teams_list


def team_stats(id_team,season_type):
    local_game = ["Home","Road",'']
    teams_list =[]
    
    for local in local_game:
        team = team_dashboard_year_by_year(id_team,season_type,local)
        teams_list.append(team)

        imp.time.sleep(1)
        
    df = imp.pd.concat(teams_list)
    
    return(df)


def team_dashboard_year_by_year(id_team,season_type,local_game):
    
    teams_list = []
    
    for month in range(0,12):
        df =  imp.teamdashboardbyyearoveryear.TeamDashboardByYearOverYear(team_id= id_team,
                                                                     location_nullable=local_game,
                                                                     per_mode_detailed="PerGame",
                                                                     pace_adjust='Y',
                                                                     month=month,
                                                                     season_type_all_star=season_type
                                                                   ).get_data_frames()[1]
      
        df['MONTH'] = month
        df["LOCAL"] = local_game
        df["TEAM_ID"] = id_team
        df['SEASON_TYPE'] = season_type
                    
        all_seasons= general.drop_and_rename_coloumns(df)
        
        teams_list.append(all_seasons)
        imp.time.sleep(1)
        
    df = imp.pd.concat(teams_list)

    return(df)

