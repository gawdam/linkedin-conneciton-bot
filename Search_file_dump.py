
#Filters
try:
    try:
        driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[1]/ul/li[1]/button/span').click()
    except:
        driver.find_element_by_xpath(
            '/html/body/div[8]/div[3]/div/div[1]/header/div/div/div[1]/ul/li[1]/button/span').click()
except:
    driver.find_element_by_id('ember953').click()

sleep(2)
# Connections
try:
    driver.find_element_by_xpath(
        '/html/body/div[8]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/button/span').click()
except:
    driver.find_element_by_xpath(
        '/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/button/li-icon').click()

sleep(1)
try:
    driver.find_element_by_xpath(
        '/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/ul/li[2]/label/p').click()
    driver.find_element_by_xpath(
        '/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/ul/li[3]/label/p').click()
except:
    driver.find_element_by_xpath(
        '/html/body/div[8]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/ul/li[2]/label').click()
    driver.find_element_by_xpath(
        '/html/body/div[8]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/ul/li[3]/label').click()
# apply
try:
    driver.find_element_by_xpath(
        '/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/div/div/button[2]/span').click()
except:
    driver.find_element_by_xpath(
        '/html/body/div[8]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/div/div/button[2]/span').click()

sleep(2)

#Next button
try:
    try:
        try:
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/button[2]/span').click()
        except:
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/button[2]/span').click()

    except:
        try:
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/button[2]/span').click()
        except:
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/button[2]/span').click()
except:
    try:
        try:
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/button[2]/li-icon').click()
        except:
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/button[2]/li-icon').click()
    except:
        try:
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/button[2]/li-icon').click()
        except:
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/button[2]/li-icon').click()
li_id = 1