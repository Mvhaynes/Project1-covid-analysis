# Data  
hospital_bed = 'https://coronavirus-resources.esri.com/datasets/1044bb19da8d4dbfb6a96eb1b4ebf629_0?geometry=110.390%2C-16.820%2C-135.352%2C72.123'
hospital_capacity = 'https://healthdata.gov/dataset/covid-19-reported-patient-impact-and-hospital-capacity-state'
uninsured_popn = 'https://data.census.gov/cedsci/table?t=Health%20Insurance&tid=ACSST1Y2019.S2702&hidePreview=false'
texas_demographics = 'https://data.census.gov/cedsci/profile?g=0400000US48'
nursing_homes = 'https://data.cms.gov/stories/s/COVID-19-Nursing-Home-Data/bkwz-xpvg'
healthdata.gov API = 'https://www.healthdata.gov/data.json?'
    deaths by county and race: https://healthdata.gov/dataset/provisional-covid-19-death-counts-county-and-race 
        json: https://healthdata.gov/dataset/provisional-covid-19-death-counts-county-and-race/resource/ba7a1f61-8ba9-40e7-9293 
excess deaths (by sex/age/race): https://healthdata.gov/dataset/ah-excess-deaths-sex-age-and-race 

# Documentation
census: https://www.census.gov/data/developers/guidance/api-user-guide.html 
arcgis: https://developers.arcgis.com/rest/services-reference/query-feature-service-layer-.htm 
cms (nursing home data): https://dev.socrata.com/foundry/data.cms.gov/s2uc-8wxp.json
    # Useful parameters: 
        # residents_weekly_confirmed
        # residents_total_all_deaths (* reports all deaths since Jan2020 regardless of cause)
        # total_resident_covid_19_deaths_per_1_000_residents  (only covid nursing home deaths)
        # county 
healthdata.gov: https://dkan.readthedocs.io/en/latest/apis/datastore-api.html 
    # Useful parameters:
        # resource_id - id (string) or ids (array) of the resource(s) to be searched against.
        # filters (mixed) – array or string of matching conditions to select
        # q (string) – fulltext search
        # limit (int) – maximum number of rows to return
