import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sys

#uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url,driver):
    driver.get(url)
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
    return soup


def main():

    #get login info from a file
    file = open('loginInfo.txt')
    login_info = []
    for line in file:
        line = line.strip()
        login_info.append(line)

    #keep browser window open after program terminates
    opts = Options()
    opts.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options=opts)

    #login
    login_url = 'https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1'
    driver.get(login_url)

    id_box = driver.find_element_by_id('netid')
    id_box.send_keys(login_info[0])

    pass_box = driver.find_element_by_id('easpass')
    pass_box.send_keys(login_info[1])

    login_button = driver.find_element_by_name('BTN_LOGIN')
    login_button.click()


    #go to registration
    registration_button = driver.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[3]/td[2]/a')
    registration_button.click()


    #go to classic registration
    classic_reg_button = driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')
    classic_reg_button.click()

    #go to add/drop classes
    add_classes_button = driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[4]/td[2]/a')
    add_classes_button.click()

    #agree to registration
    agree_button = driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a')
    agree_button.click()

   
    #select term for registration, default is the latest term
    term_button = driver.find_element_by_xpath('//*[@id="term_id"]/option[1]')
    
    submit_button = driver.find_element_by_xpath('/html/body/div[3]/form/input')
    submit_button.click()

    #read crn's from a file
    file = open('crns.txt')
    crns = []
    for line in file:
        line = line.strip()
        crns.append(line)

    #add crns to class worksheet
    for i in range(len(crns)):
        id_str = '//*[@id="crn_id' + str(i + 1) + '"]'
        box = driver.find_element_by_xpath(id_str)
        box.send_keys(crns[i])

    #submit class worksheet
    submit_button = driver.find_element_by_xpath('/html/body/div[3]/form/input[19]')
    submit_button.click()

    #TODO: retry to register if classes failed
    


if __name__ == '__main__':
    main()