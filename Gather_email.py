from selenium import webdriver
from password import username,password
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
#from Profiles import top_companies
import xlsxwriter
from bs4 import BeautifulSoup
from time import sleep


driver = webdriver.Firefox()

#create file
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

#Login
driver.get('https://www.linkedin.com/uas/login')
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button').click()


#GoToProfile
driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[6]/div/div/button/div/li-icon').click()
driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[6]/div/div/div/div/ul/li[1]/a/div[2]/span').click()
driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[6]/div/div/button/div/li-icon').click()


#Open connections
sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[2]/a/span').click()


i = 0
li_id = 10


while i < 50:
    if li_id>10:
        li_id = 1
        sleep(3)
        act = ActionChains(driver)
        act.send_keys(Keys.PAGE_DOWN).perform()
        act.send_keys(Keys.PAGE_DOWN).perform()
        sleep(2)
        try:
            try:
                try:
                    driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/button[2]/span').click()
                    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                except:
                    driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/button[2]/span').click()
            except:
                try:
                    driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/button[2]/li-icon').click()
                except:
                    driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/button[2]/li-icon').click()
        except:
            break


        sleep(3)

    sleep(5)
    try:
        try:
            driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li['+str(li_id)+']/div/div/div[2]/a/h3/span/span/span[1]').click()
            ''
        except:
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li['+str(li_id)+']/div/div/div[2]/a/h3/span/span/span[1]').click()

    except:
        act = ActionChains(driver)
        act.send_keys(Keys.PAGE_DOWN).perform()
        sleep(3)
        try:
            driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[' + str(li_id) + ']/div/div/div[2]/a/h3/span/span/span[1]').click()
        except:
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li['+str(li_id)+']/div/div/div[2]/a/h3/span/span/span[1]').click()

    li_id = li_id+1
    linkedin_id = driver.current_url
    sleep(3)
    #name
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    try:
        name_div = soup.find('div',{'class': 'flex-1 mr5'})
        name_loc = name_div.find_all('ul')
        name = name_loc[0].find('li').get_text().strip()
    except:
        name = "Unable to find"

    #Open_contact info
    try:
        driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[3]/a/span').click()
        sleep(2)
        src2 = driver.page_source
        soup2 = BeautifulSoup(src2, 'lxml')
        try:
            email_loc = soup2.find('section', {'class': 'pv-contact-info__contact-type ci-email'})
            email_loc = email_loc.find('a',{'class':'pv-contact-info__contact-link t-14 t-black t-normal'})
            email = email_loc.get_text().strip()
        except:
            email = "NA"
        try:
            ph_loc = soup2.find('section',{'class':'pv-contact-info__contact-type ci-phone'})
            ph_loc = ph_loc.find('li', {'class':'pv-contact-info__ci-container t-14'})
            ph_no = ph_loc.find('span').get_text().strip()
        except:
            ph_no = "NA"
        driver.back()
    except:
        email = "CONTACT/NA"
        ph_no = "CONTACT/NA"



    #experience
    try:
        exp_section = soup.find('section',{'id':'experience-section'})
        exp_section = exp_section.find('ul')
        li_tags = exp_section.find('div')
        a_tags = li_tags.find('a')
        try:
            job_title = a_tags.find('h3').get_text().strip()
            company_name = a_tags.find_all('p')[1].get_text().strip()
            exp = a_tags.find_all('h4')[1].find_all('span')[1].get_text().strip()
        except:
            div_tags = a_tags.find('div')
            job_title= exp_section.find_all('span')[6].get_text().strip()
            company_name = div_tags.find('h3').find_all('span')[1].get_text().strip()
    except:
            company_name = "NA"
            job_title = "NA"


    #education
    try:
        edu_section = soup.find('section', {'id': 'education-section'}).find('ul')
        college_name = edu_section.find('h3').get_text().strip()
        degree = edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
    except:
        college_name = "NA"
        degree = "NA"
    try:
        graduation = edu_section.find('p',{'class':'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[1].get_text().strip()
        graduation = graduation[-4:-1]+graduation[-1]
        exp = 2020-int(graduation)
        exp = str(exp)
        exp = exp + '+'
    except:
        exp = "~~~"

    #export
    print(name)
    print(company_name)
    print(job_title)
    print(degree)
    print(exp)
    print(email)
    print(ph_no)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    worksheet.write(i, 0 , name)
    worksheet.write(i, 1 , linkedin_id)
    worksheet.write(i, 2 , datetime.today().strftime('%m-%d-%Y'))
    worksheet.write(i, 3 , company_name)
    worksheet.write(i, 4 , job_title)
    worksheet.write(i, 5 , degree + ',' + college_name)
    worksheet.write(i, 6 , exp)
    worksheet.write(i, 7 , email)
    worksheet.write(i, 8 ,ph_no)
    driver.back()
    i = i+1
    print(i)
workbook.close()
print('done')