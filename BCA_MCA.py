from selenium import webdriver
from password import username2, password2
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from Database import top_companies, top_universities
from bs4 import BeautifulSoup
from time import sleep
from fuzzywuzzy import process,fuzz
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google_sheets_updation
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("LinkedIn_leads.json", scope)
client = gspread.authorize(creds)
worksheet = client.open('LiBOT_Searches').get_worksheet(0)

driver = webdriver.Firefox()


# Login
driver.get('https://www.linkedin.com/uas/login')
driver.find_element_by_id('username').send_keys(username2)
driver.find_element_by_id('password').send_keys(password2)
driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button').click()

# Search


# Filters
page = 1
search_url = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22in%3A0%22%5D&facetNetwork=%5B%22S%22%2C%22O%22%5D&keywords=Web%20application&origin=GLOBAL_SEARCH_HEADER&page='
driver.get(search_url+str(page))
# id of the searched person
li_id = 1
i = 1
curr_row = 638

while i < 28:
    #update the search url
    sleep(5)

    #move to next page if all profiles are visited
    if li_id > 10:
        page += 1
        act = ActionChains(driver)
        act.send_keys(Keys.PAGE_DOWN).perform()
        act.send_keys(Keys.PAGE_DOWN).perform()
        sleep(5)
        try:
            driver.get(search_url+str(page))
            li_id = 1
        except:
            pass

        sleep(3)

    #Go into profile
    try:
        try:
            driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[' + str(li_id) + ']/div/div/div[2]/a/h3/span/span/span[1]').click()

        except:
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[' + str(li_id) + ']/div/div/div[2]/a/h3/span/span/span[1]').click()

    except:
        try:
            act = ActionChains(driver)
            act.send_keys(Keys.PAGE_DOWN).perform()
            sleep(3)
            try:
                driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[' + str(li_id) + ']/div/div/div[2]/a/h3/span/span/span[1]').click()
            except:
                driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[' + str(li_id) + ']/div/div/div[2]/a/h3/span/span/span[1]').click()
        except:
            pass

    li_id = li_id + 1
    sleep(3)
    linkedin_id = driver.current_url

    # name
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    try:
        name_div = soup.find('div', {'class': 'flex-1 mr5'})
        name_loc = name_div.find_all('ul')
        name = name_loc[0].find('li').get_text().strip()
    except:
        name = "Unable to find"

    #Experience
    try:
        exp_section = soup.find('section', {'id': 'experience-section'})
        exp_section = exp_section.find('ul')
        li_tags = exp_section.find('div')
        a_tags = li_tags.find('a')
        try:
            job_title = a_tags.find('h3').get_text().strip()
            company_name = a_tags.find_all('p')[1].get_text().strip()
            exp = a_tags.find_all('h4')[1].find_all('span')[1].get_text().strip()
        except:
            div_tags = a_tags.find('div')
            job_title = exp_section.find_all('span')[6].get_text().strip()
            company_name = div_tags.find('h3').find_all('span')[1].get_text().strip()

    except:
        company_name = "NA"
        job_title = "NA"
    if " " in company_name:
        company_name = company_name.split()[0]

    # education
    college_name = []
    try:
        edu_section = soup.find('section', {'id': 'education-section'}).find('ul')
        college_name.append(edu_section.find('h3').get_text().strip())
        try:
            college_name.append(edu_section.find_all('h3')[1].get_text().strip())
            try:
                college_name.append(edu_section.find_all('h3')[2].get_text().strip())
            except:
                pass
        except:
            pass
        degree = edu_section.find('p', {'class': 'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
    except:
        college_name.append("NA")
        degree = "NA"
    try:
        graduation = edu_section.find('p', {'class': 'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[
            1].get_text().strip()
        graduation = graduation[-4:-1] + graduation[-1]
        exp = 2020 - int(graduation)
    except:
        exp = 0

    #See if already connected
    Connect_flag = 0
    connection_status = "Pending"
    try:

        try:
            div_tags = soup.find('div', {'class': 'flex-1 flex-column display-flex mt3 mb1'})
            connection_status = div_tags.find("span",{"class":'artdeco-button__text'}).get_text().strip()
        except:
            try:
                driver.find_element_by_xpath(
                    '/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button/span').click()
            except:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button/span').click()
                sleep(2)
            connection_status = soup.find_all('span', {'class': 'display-flex t-normal pv-s-profile-actions__label'})[3].get_text().strip()
        if connection_status == "Connect":
            Connect_flag = 1
        else:
            Connect_flag = 0

    except:
        pass


    confidence_level = 1


    # export
    if exp > 3 and name != "Unable to find":

        # Confidence Level
        comm = []
        comment = " "
        # Company & Experience
        if exp > 5:
            confidence_level += 1
        if exp > 10:
            confidence_level += 2
            comm.append("Great experience")
        if process.extractOne(company_name,top_companies)[1]>80:
            confidence_level += 2
            comm.append("Good company")

        # Job role
        if fuzz.partial_ratio("Senior".lower(),job_title.lower())>95:
            confidence_level +=1
            comm.append("Senior role")

        # Degree: PhD and M.tech
        if degree[0] == 'M' or degree[0] == 'm':
            confidence_level += 0.5
            comm.append("Good education")
        elif degree[0] == 'P' or degree[1] == 'p':
            confidence_level += 1
            comm.append("Great education")

        #T-1/T-2 checker
        num = []
        for j in range(len(college_name)):
            num.append(process.extractOne(college_name[j],top_universities)[1])

        ratio = max(num)
        j = num.index(ratio)

        # University
        if ratio > 87:
            confidence_level += 1
            comm.append("Good university")

        #Confidence %
        confidence_level = confidence_level/8*100

        #Assign POC
        PoC = "Shraddha"

        if confidence_level >= 50 and Connect_flag:


            #Add to sheet
            worksheet.update_cell(curr_row, 1, name)
            worksheet.update_cell(curr_row, 2, linkedin_id)
            worksheet.update_cell(curr_row, 5, 'LinkedIn')
            worksheet.update_cell(curr_row, 6, datetime.today().strftime('%m-%d-%Y'))
            worksheet.update_cell(curr_row, 7, PoC)
            worksheet.update_cell(curr_row, 19, company_name)
            worksheet.update_cell(curr_row, 20, job_title)
            worksheet.update_cell(curr_row, 21, degree + ',' + college_name[j])
            worksheet.update_cell(curr_row, 22, str(exp) + '+')
            worksheet.update_cell(curr_row, 25, str(confidence_level)+'%')
            worksheet.update_cell(curr_row, 27 ,comment.join(comm))
            worksheet.update_cell(curr_row, 32 ,page)
            i = i + 1
            curr_row = curr_row + 1
            print(i)
            print("ACCEPTED")
        elif Connect_flag == 0:
            print("PENDING/WAITING TO ACCEPT")
        else:
            print("REJECTED")
        print(name)
        print(company_name)
        print(job_title)
        print(degree)
        print(exp)
        print("Page = ", page)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    driver.back()
print('done')
