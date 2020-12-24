import selenium
from selenium import webdriver 
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


#uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url,driver):
    driver.get(url)
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
    return soup


def main():

    #get login info
    file = open('loginInfo.txt')
    login_info = []
    for line in file:
        line = line.strip()
        login_info.append(line)

    driver = webdriver.Chrome()

    login_url = 'https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1'
    driver.get(login_url)

    id_box = driver.find_element_by_id('netid')
    id_box.send_keys(login_info[0])

    pass_box = driver.find_element_by_id('easpass')
    pass_box.send_keys(login_info[1])

    login_button = driver.find_element_by_name('BTN_LOGIN')
    login_button.click()


    '''
    soup = get_js_soup(driver.current_url, driver)
    for line in soup.find_all('td', class_='pldefault'):
        message = line.find('b')
        if message != "":
            print(message)
    

    print(driver.current_url)
    '''

    #registration_button = driver.find_element_by_partial_link_text('SITE MAP')
    #registration_button.click()

    wait = WebDriverWait(driver, 10)
    registration_button = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Records')))
    registration_button.click()
    print("here")
   


if __name__ == '__main__':
    main()