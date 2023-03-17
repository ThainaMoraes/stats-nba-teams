# stats-nba-teams

<h1>THE DASHBOARD</h1>

This dashboard aimed to facilitate the average performance of each team during all seasons in which there is data collected. It's possible to visualize the metrics (traditional and some advanced) and some correlations between them.


The dashboard was divided into three different forms of analysis:

  1. Team vs Opponent - The statistics of the team in relation to its opponent;
  2. Team Stats - Overall team stats, without a specific opponent;
  3. Ranking - Ranking of top 5 teams given six metrics analyzed individually.


On all pages the following filters are available:

  - Seasons;
  - Local Game;
  - Season Type;
  - Month*.
  
 <h1> DATA COLLECTION </h1>

1) I used the nba_api to collect the data.
For Team vs Opponent,  I used two main functions to do the queries: teamdashboardbyyearoveryear and teamdashboardbyopponent.
    - For the teamdashboardbyyearoveryear  it was only used to find all the seasons that a given team played.
    - In teamdashboardbyopponent there are variations of the parameters: location_nullbable, season, season_type_all_star; and the fixed parameters per query for each team: team_id, per_mode_detailed, pace_adjust.

2) For Team Stats and Ranking,  I used teamdashboardbyyearoveryear.

    - Just changing the parameters: location_nullbable, season_type_all_star, month; and using fixed parameters per query for each team: team_id, per_mode_detailed, pace_adjust.
    
<h1> IMPORTANT INFORMATION</h1> 

All data is normalized so the comparison between two teams is done fairly.

<h1> THE CHALLENGES</h1> 

This was the first project that I decide to do by myself. So I chose to analyze the NBA Teams during all seasons because I started watching basketball games and I enjoyed it. 

My first big challenge was to decide what kind of information was more relevant to analyze. So I chose to use the traditional stats. I also used three advanced stats, because they were able to calculate with the data I already had. 

Another big challenge for me was to build a clean and useful dashboard, with a good user experience. I discovered Figma and this was my first project using this interface design tool. 
