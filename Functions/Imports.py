#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nba_api
import time
from zipfile import ZipFile
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamdashboardbyopponent
from nba_api.stats.endpoints import teamdashboardbyyearoveryear

pd.set_option("display.max_columns", None)

