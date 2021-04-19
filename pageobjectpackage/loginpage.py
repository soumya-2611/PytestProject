from selenium import webdriver
import time
class Login:
    textbox_username_id= "Email"
    textbox_password_id="Password"
    button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_xpath="//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()#clear the textbox
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def clicklogin(self):

        self.driver.find_element_by_xpath(self.button_login_xpath).click()


    def logout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()
        time.sleep(4)


