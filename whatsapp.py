from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WhatsAppHelper:

    send_button_xpath = '//span[@data-testid = "send"]'
    attachment_xpath = '//span[@data-testid = "clip"]'
    message_box_xpath = '//div[@data-testid="conversation-compose-box-input"]'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        self.driver.maximize_window()

    def click_on_send(self):
        send = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH ,self.send_button_xpath)))

    def attach_message(self,message):
        msg_box = self.driver.find_element(by = By.XPATH , value = self.message_box_xpath)
        msg_box.send_keys(message)