from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Create your tests here.


class RegisterFormTest(LiveServerTestCase):

    def test_registration(self):
        rand_num = random.randrange(1000)
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/accounts/register')

        username = selenium.find_element(By.ID, "id_username")
        password1 = selenium.find_element(By.ID, "id_password1")
        password2 = selenium.find_element(By.ID, "id_password2")
        email = selenium.find_element(By.ID, "id_email")
        phone = selenium.find_element(By.ID, "id_advisor_phone_number")
        first_name = selenium.find_element(By.ID, "id_first_name")
        last_name = selenium.find_element(By.ID, "id_last_name")

        register_button = selenium.find_element(By.CLASS_NAME, "btn-primary")


        username.send_keys(f"unique_username_{rand_num}")
        password1.send_keys("nereuss90eh543hql34ijh")
        password2.send_keys("nereuss90eh543hql34ijh")
        email.send_keys(f"test_email{rand_num}@geemail.com")
        phone.send_keys("2089696988")
        first_name.send_keys("Bort")
        last_name.send_keys("Sampson")

        register_button.send_keys(Keys.RETURN)
        
        element = WebDriverWait(selenium, 100).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))

             )
        assert element.text == 'Login Here'


    # def test_login(self):
        
