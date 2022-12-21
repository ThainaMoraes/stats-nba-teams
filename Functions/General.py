#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Functions.Imports as imp


# In[ ]:


def drop_and_rename_coloumns(df_season):

    list_columns = ["CFID","CFPARAMS","GROUP_SET"]
    
    for item in df_season.columns:
            
            if "RANK" in item:
                list_columns.append(item)
                
    all_seasons = df_season.drop(columns = list_columns)
    all_seasons.rename(columns = {"GROUP_VALUE" : "SEASON"}, inplace = True)
        
    return all_seasons


# In[ ]:


def save_zip_file(name_zip_file, teams_list_or_df, list_or_df = "LIST", save_nba_teams = "Y"):
  
    with imp.ZipFile(f"{name_zip_file}.zip", "w") as zf:
        
        if save_nba_teams == "Y":
            nba_teams = imp.teams.get_teams()
            
            with zf.open("nba_teams.csv", "w") as buffer:
                
                nba_teams_df = imp.pd.DataFrame(nba_teams)
                nba_teams_df.to_csv(buffer,index=False)
        
        if list_or_df == "LIST":
            count = 0
            
            for df in teams_list_or_df:
                id_team = df['TEAM_ID'].unique()[0]

                with zf.open(f"{id_team}.csv", "w") as buffer:
                    df.to_csv(buffer,index=False)

                count = count+1
                        
        else:
            with zf.open("all_teams.csv", "w") as buffer:
                    teams_list_or_df.to_csv(buffer,index=False)


# In[ ]:


def open_zip_file(name_zip_file):
    
    with imp.ZipFile(f'{name_zip_file}.zip', 'r') as zipObj:
        name_files = zipObj.namelist()
        
    dfs_zip_file = from_zip_file(name_zip_file)
    
    teams = []
    for i in name_files:
        teams.append(dfs_zip_file[i])
        
    return teams


# In[ ]:


def from_zip_file(name_zip_file):
    
    zip_file = imp.ZipFile(f"{name_zip_file}.zip")

    dfs_zip_file = {text_file.filename:
                    imp.pd.read_csv(zip_file.open(text_file.filename))
                    for text_file in zip_file.infolist()
                    if text_file.filename.endswith(".csv")}
    
    return(dfs_zip_file)


# In[ ]:


def open_and_join_files(file_name, list_join_teams):
    
    teams_dfs = dfs_teams_from_zip_file(f"{file_name}")
    join_teams = imp.pd.concat(teams_dfs)
    list_join_teams.append(join_teams)
    
    return list_join_teams


# In[ ]:


def dfs_teams_from_zip_file(name_zip_file):
    
    with imp.ZipFile(f'{name_zip_file}.zip', 'r') as zipObj:
        name_files = zipObj.namelist()
        
    dfs_zip_file = from_zip_file(name_zip_file)
    
    teams = []
    for i in name_files:
        teams.append(dfs_zip_file[i])
        
    return teams


# In[ ]:


def modify_columns(list_dfs,opponent = "N"):
   
    if opponent == "N":
        
        month = {0:'All',1:"October",2:"November",3:"December",4:"January",5:"February",6:"March",7:"April",8:"May",9:"June",10:"July",11:"August"}
        
        for df in list_dfs:
#             df.rename(columns={"OPPONENT": "SEASON"},inplace = True)
            
            df.fillna("All",inplace=True)
            df.replace({"MONTH": month},inplace=True)
            df["DATA"] = df["MONTH"].astype(str) + "/" + df["SEASON"].str.slice(0,4)
        
    for df in list_dfs:
        
        df.fillna("All",inplace=True)
        
        df["FG2M"] = df["FGM"] - df["FG3M"]
        df["FG2A"] = df["FGA"] - df["FG3A"]
        df["FG2_PCT"] = df["FG2M"]/df["FG2A"]
        
        df["3PTS"] = (df["FG3M"]*3)
        df["2PTS"] = (df["FG2M"]*2)  
        

