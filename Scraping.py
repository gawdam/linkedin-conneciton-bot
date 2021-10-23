from selenium import webdriver
from password import username,password
from Database import profiles2
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

#loop
for i in range(len(profiles2)):
    #gotoURL
    driver.get(profiles2[i])

    #name
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    name_div = soup.find('div',{'class': 'flex-1 mr5'})
    name_loc = name_div.find_all('ul')
    name = name_loc[0].find('li').get_text().strip()

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

    worksheet.write(i, 0, name)
    worksheet.write(i, 15, company_name)
    worksheet.write(i, 16, job_title)
    worksheet.write(i, 17, degree + ',' + college_name)
    worksheet.write(i, 18, exp)

    #Connect with a custom message
    try:
        driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button/span').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]/span').click()
        driver.find_element_by_xpath('//*[@id="custom-message"]').send_keys('Hello ' + name.split()[0] + ',' + '\n' + 'I would like to connect with you')
        #driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]/span').click()
    except:
        try:
            driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button/span').click()
            driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div/li-icon').click()
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]/span').click()
            driver.find_element_by_xpath('//*[@id="custom-message"]').send_keys('Hello ' + name.split()[0] + ',' + '\n' + 'I would like to connect with you')
            #driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]/span').click()
        except:
            #If unable to connect
            print("Already connected/Not able to connect")
    print(name)
    sleep(20)
workbook.close()

print('done')