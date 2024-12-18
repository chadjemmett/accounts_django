from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Create your tests here.
PASSWORD = "MobbV@Ms368eZiMmXWF_f4qnZJa"

class RegisterFormTest(LiveServerTestCase):
    
    selenium = webdriver.Chrome()

    def test_registration(self):
        rand_num = random.randrange(1000)
        self.selenium.get('http://127.0.0.1:8000/accounts/register')

        username = self.selenium.find_element(By.ID, "id_username")
        password1 = self.selenium.find_element(By.ID, "id_password1")
        password2 = self.selenium.find_element(By.ID, "id_password2")
        email = self.selenium.find_element(By.ID, "id_email")
        phone = self.selenium.find_element(By.ID, "id_advisor_phone_number")
        first_name = self.selenium.find_element(By.ID, "id_first_name")
        last_name = self.selenium.find_element(By.ID, "id_last_name")

        register_button = self.selenium.find_element(By.CLASS_NAME, "btn-primary")


        username.send_keys(f"unique_username_{rand_num}")
        password1.send_keys(PASSWORD)
        password2.send_keys(PASSWORD)
        email.send_keys(f"test_email{rand_num}@geemail.com")
        phone.send_keys("2089696988")
        first_name.send_keys("Bort")
        last_name.send_keys("Sampson")

        register_button.send_keys(Keys.RETURN)
        
        element = WebDriverWait(self.selenium, 100).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))

             )
        assert element.text == 'Dashboard'


    def test_login(self):
        self.selenium.get('http://127.0.0.1:8000/accounts/login')
        username = self.selenium.find_element(By.ID, "id_username")
        password = self.selenium.find_element(By.ID, "id_password")
        
        login_button = self.selenium.find_element(By.ID, "submit_id")

        username.send_keys("test_username")
        password.send_keys(PASSWORD)
        login_button.send_keys(Keys.RETURN)

        element = WebDriverWait(self.selenium, 100).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))

             )
        print(element)
        assert element.text == 'Dashboard'
        self.selenium.close()
