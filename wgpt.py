from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsappHelper:
    def _init_(self):
        self.driver = webdriver.Chrome() # Replace with your preferred browser driver

        # Wait for Whatsapp web page to load
        self.driver.get("https://web.whatsapp.com/")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="app _1RiQ7"]')))
        
        # Locate important elements on the page using their xpaths
        self.search_box_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@data-tab="3"]'
        self.search_button_xpath = '//button[@class="_2Ujuu"]'
        self.chat_name_xpath = '//div[@class="3ko75 _5h6Y _3Whw5"]'
        self.chat_input_xpath = '//div[@class="_3uMse"][@contenteditable="true"][@data-tab="1"]'
        self.send_button_xpath = '//span[@data-testid="send"]'
        self.attach_button_xpath = '//div[@title="Attach"]'
        self.image_button_xpath = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
        self.send_image_button_xpath = '//span[@data-icon="send-light"]'

    def send_text(self, chat_name, message):
        # Search for the chat by name
        search_box = self.driver.find_element_by_xpath(self.search_box_xpath)
        search_box.clear()
        search_box.send_keys(chat_name)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

        # Wait for chat to load and locate the chat input box
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.chat_name_xpath.format(chat_name))))
        chat_input = self.driver.find_element_by_xpath(self.chat_input_xpath)

        # Enter the message and send it
        chat_input.send_keys(message)
        self.driver.find_element_by_xpath(self.send_button_xpath).click()

    def send_image(self, chat_name, image_path):
        # Search for the chat by name
        search_box = self.driver.find_element_by_xpath(self.search_box_xpath)
        search_box.clear()
        search_box.send_keys(chat_name)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

        # Wait for chat to load and locate the attach button
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.chat_name_xpath.format(chat_name))))
        self.driver.find_element_by_xpath(self.attach_button_xpath).click()

        # Locate and upload the image file
        image_button = self.driver.find_element_by_xpath(self.image_button_xpath)
        image_button.send_keys(image_path)

        # Wait for the image to upload and locate the send button
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.send_image_button_xpath)))
        self.driver.find_element_by_xpath(self.send_image_button_xpath).click()

    def quit(self):
        self.driver.quit()