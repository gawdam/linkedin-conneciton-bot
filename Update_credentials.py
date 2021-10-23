import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("LinkedIn_leads.json",scope)
client = gspread.authorize(creds)

sheet = client.open('SD 2.0 Tracker').get_worksheet(2)

https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22in%3A0%22%5D&facetNetwork=%5B%22S%22%2C%22O%22%5D&keywords=System%20architect&origin=GLOBAL_SEARCH_HEADER&page=13