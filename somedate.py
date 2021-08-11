from datetime import date, datetime, timedelta
import requests
import json

from datetime import date, timedelta


# ------------- INSERT CRON JOB FOR AUTOMATIC DATES ----------\
# with open('/home/freddy/covid19/final.json', 'rb') as check_date:
#     file_check = json.load(check_date)
#     print(file_check[-1]["day"])

sdate = date(2021, 8, 6)   # start date
edate = date.today() - timedelta(1) # end date
delta = edate - sdate       # as timedelta

daylist = []
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    daylist.append(str(day))

for oneday in daylist:
    url = f"https://covid-193.p.rapidapi.com/history?country=kenya&day={oneday}"
    headers = {
    'x-rapidapi-key': "6672acff71msha2668ee10af537bp1245a2jsn31635e6b6758",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    querystring = {"country": "kenya"}
    response = requests.request("GET", url, headers=headers, params=querystring).text
    our_json_data = json.loads(response)
    new_json_data = our_json_data['response'][0]

    nnew_cases = int(new_json_data['cases']['new'][1:])
    aactive_cases = new_json_data['cases']['active']
    ccritical_cases = new_json_data['cases']['critical']
    rrecovered = new_json_data['cases']['recovered']
    ttotal_cases = new_json_data['cases']['total']
    nnew_deaths = int(new_json_data['deaths']['new'][1:])
    ttotal_deaths = new_json_data['deaths']['total']


    def write_json(new_data, filename='final.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data.append(new_data)
            file.seek(0)
            json.dump(file_data, file, separators=(',', ':'))
    
    our_data_list = {"new_cases":float("{0:.1f}".format(nnew_cases)),"active_cases":float("{0:.1f}".format(aactive_cases)),"critical_cases":float("{0:.1f}".format(ccritical_cases)),"recovered":float("{0:.1f}".format(rrecovered)),"total_cases":float("{0:.1f}".format(ttotal_cases)),"new_deaths":float("{0:.1f}".format(nnew_deaths)),"total_deaths":float("{0:.1f}".format(ttotal_deaths)),"day":new_json_data['day']}
    write_json(our_data_list)

