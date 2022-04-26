from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://webclient.polyvizor.com'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)


def authorization():
    email = driver.find_element(by=By.ID, value='email')
    email.send_keys('kalyadin.maksim@mail.ru')
    password = driver.find_element(by=By.ID, value='password')
    password.send_keys('42MAKS012530')
    btn = driver.find_element(by=By.CLASS_NAME, value='auth-button')
    btn.click()


def call():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-contact')
    btn_toggle_contact.click()
    time.sleep(2)
    btn_call = driver.find_elements(by=By.ID, value='call')[0]
    btn_call.click()


def stop_call():
    btn_call_stop = driver.find_element(by=By.ID, value='stop_call')
    btn_call_stop.click()


def select_new_video():
    video = driver.find_elements(by=By.CLASS_NAME, value='preview')[1]
    video.click()


def open_panel_setting():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-settings')
    btn_toggle_contact.click()
    time.sleep(2)
    select = driver.find_element(by=By.TAG_NAME, value='mat-select')
    select.click()
    time.sleep(1)
    option = driver.find_element(by=By.TAG_NAME, value='mat-option')
    option.click()


def repeat_call():
    label_tab_2 = driver.find_element(by=By.ID, value='calls')
    label_tab_2.click()
    btn_update = driver.find_element(by=By.ID, value='update')
    btn_update.click()
    time.sleep(5)
    btn_call = driver.find_element(by=By.ID, value='call_repeat')
    btn_call.click()


def repeat_call_stop():
    btn_stop_call = driver.find_element(by=By.ID, value='cal_stop_repeat')
    btn_stop_call.click()


def logout():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-settings')
    btn_toggle_contact.click()
    time.sleep(2)
    btn_logout = driver.find_element(by=By.ID, value='logout')
    btn_logout.click()


def click_href():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-settings')
    btn_toggle_contact.click()
    time.sleep(2)
    label_tab_2 = driver.find_element(by=By.ID, value='infos')
    label_tab_2.click()
    time.sleep(2)
    href = driver.find_element(by=By.TAG_NAME, value='a')
    href.click()


def search():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-contact')
    btn_toggle_contact.click()
    time.sleep(2)
    input_message = driver.find_element(by=By.ID, value='message')
    input_message.send_keys('Прям')


def mute_output():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-settings')
    btn_toggle_contact.click()
    time.sleep(2)
    btn_out = driver.find_element(by=By.ID, value='volume_output')
    btn_out.click()

    
def mute_input():
    btn_toggle_contact = driver.find_element(by=By.CLASS_NAME, value='button-toggle-settings')
    btn_toggle_contact.click()
    time.sleep(2)
    btn_inp = driver.find_element(by=By.ID, value='volume_input')
    btn_inp.click()


time.sleep(5)
authorization()
time.sleep(5)
mute_output()
time.sleep(5)
mute_input()

time.sleep(12222)
