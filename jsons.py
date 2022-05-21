countryName = []
eprtrSectorName = []
EPRTRAnnexIMainActivityLabel = []
FacilityInspireID = []
facilityName = []
City =[]
targetRelease = []
pollutant = []
reportingYear = []
MONTH= []
DAY = []
CONTINENT= []
max_wind_speed =[]
avg_wind_speed= []
min_wind_speed = []
max_temp = []
avg_temp= []
min_temp=[]
FOGDAYS=[]
CITYID = []
url1 = 'http://schneiderapihack-env.eba-3ais9akk.us-east-2.elasticbeanstalk.com/first'
url2 = 'http://schneiderapihack-env.eba-3ais9akk.us-east-2.elasticbeanstalk.com/second'
url3 = 'http://schneiderapihack-env.eba-3ais9akk.us-east-2.elasticbeanstalk.com/third'
urls = [url1,url2,url3]
for url in urls: 

    from urllib.request import urlopen

    # import json
    import json
    # store the URL in url as 
    # parameter for urlopen
    url = url

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    
    for jsons in data_json:
        countryName.append(jsons.get('countryName'))
        eprtrSectorName.append(jsons.get('eprtrSectorName'))
        EPRTRAnnexIMainActivityLabel.append(jsons.get('EPRTRAnnexIMainActivityLabel'))
        FacilityInspireID.append(jsons.get('FacilityInspireID'))
        facilityName.append(jsons.get('facilityName'))
        City.append(jsons.get('City'))
        targetRelease.append(jsons.get('targetRelease'))
        pollutant.append(jsons.get('pollutant'))
        reportingYear.append(jsons.get('reportingYear'))
        MONTH.append(jsons.get('MONTH'))
        DAY.append(jsons.get('DAY'))
        CONTINENT.append(jsons.get('CONTINENT'))
        max_wind_speed.append(jsons.get('max_wind_speed'))
        avg_wind_speed.append(jsons.get('avg_wind_speed'))
        min_wind_speed.append(jsons.get('min_wind_speed'))
        max_temp.append(jsons.get('max_temp'))
        avg_temp.append(jsons.get('avg_temp'))
        min_temp.append(jsons.get('min_temp'))
        FOGDAYS.append(jsons.get('DAY WITH FOGS'))
        CITYID.append(jsons.get('CITY ID'))

    
df_json = pd.DataFrame({'countryName':countryName,
                        'eprtrSectorName':eprtrSectorName,
                        'EPRTRAnnexIMainActivityLabel':EPRTRAnnexIMainActivityLabel,
                        'FacilityInspireID':FacilityInspireID,
                        'facilityName':facilityName,
                        'City':City,
                        'targetRelease':targetRelease,
                        'pollutant':pollutant,
                        'reportingYear':reportingYear,
                        'MONTH':MONTH,
                        'DAY':DAY,
                        'CONTINENT':CONTINENT,
                        'max_wind_speed':max_wind_speed,
                        'avg_wind_speed':avg_wind_speed,
                        'min_wind_speed':min_wind_speed,
                        'max_temp':max_temp,
                        'avg_temp':avg_temp,
                        'min_temp': min_temp,
                        'FOGDAYS':FOGDAYS,
                        'CITYID':CITYID})
    
