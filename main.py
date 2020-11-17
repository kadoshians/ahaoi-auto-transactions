from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import random

class AutoTransaction:

    def __init__(self, config, data):
        """
        Parameter initialisation
        """
        self.email = config['email']
        self.password = config['password']
        self.user_amount = config['user_amount']
        self.persons = data['persons']
        self.amounts = data['amounts']
        self.driver = webdriver.Chrome(config['driver_path']


        )


    def login_ahoi(self):
        """
        docstring
        """

        self.driver.get("https://banking-sandbox.starfinanz.de/sandboxmanager/#/login")

        # introduce email and password and hit enter
        login_email = self.driver.find_element_by_id('input-email')
        login_email.clear()
        login_email.send_keys(self.email)
        login_pass = self.driver.find_element_by_id('input-password')
        login_pass.clear()
        login_pass.send_keys(self.password)
        login_pass.send_keys(Keys.RETURN)

    def new_transaction(self):

        self.driver.find_element_by_link_text("DE00 9999 4000 0000 0025 85").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[@id='add-transaction']/div").click()
        time.sleep(2)

        for _ in range(self.user_amount):
            person, iban = self.persons[random.randrange(len(self.persons))][0], self.persons[random.randrange(len(self.persons)+1)][1]
            amount = self.amounts[random.randrange(len(self.amounts))]

            input_name = self.driver.find_element_by_id("input-name")
            time.sleep(3)
            input_name.send_keys(person)
            time.sleep(3)

            input_iban = self.driver.find_element_by_id("input-iban")
            time.sleep(4)
            input_iban.send_keys(iban)
            time.sleep(4)

            input_bic =  self.driver.find_element_by_id("input-bic")
            time.sleep(3)
            input_bic.send_keys("TBICXXXX")
            time.sleep(4)

            input_purpose = self.driver.find_element_by_id("input-purpose")
            time.sleep(4)
            input_purpose.send_keys("Essen-Trinken")
            time.sleep(4)

            input_amount = self.driver.find_element_by_id("input-amount")
            time.sleep(4)
            input_amount.send_keys(amount)
            time.sleep(2)


            self.driver.find_element_by_id("button-add-transaction").click()


    def go(self):
        self.login_ahoi()
        time.sleep(3)
        self.new_transaction()
        self.driver.close()

    


if __name__ == '__main__':

    with open('config.json') as config_file:
        config = json.load(config_file)
    
    with open('generate_users/user.json') as data_file:
        data = json.load(data_file)

    bot = AutoTransaction(config, data)
    bot.go()