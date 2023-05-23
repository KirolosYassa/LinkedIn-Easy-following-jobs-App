import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class LinkedIn():
    def __init__(self, url="https://www.linkedin.com/"):
        load_dotenv()   
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.url = url
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.driver.get(url)


    def signin(self):
        sign_in = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
        sign_in.click()

        username_form = self.driver.find_element(By.ID, 'username')
        username_form.send_keys(self.email)
        password_form = self.driver.find_element(By.ID, 'password')
        password_form.send_keys(self.password)

        sign_in_in_form = self.driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
        sign_in_in_form.click()
        time.sleep(4.2)
        
        
    
    def get_jobs_list(self):
        self.job_lists = self.driver.find_elements(By.CSS_SELECTOR, "a.job-card-list__title")
        for job in self.job_lists:
            print(job.text)
        return self.job_lists
    
    def click_specific_job(self, job_index=0):
        self.job_lists[job_index].click()
        time.sleep(0.5)
        
            
    def save_job(self):
        save_button = self.driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")
        save_button.click()
        time.sleep(0.5)
    
    def follow_selected_job_company(self):
        company = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]')
        print(f"company = {company.text}")
        company.click()
        time.sleep(2.5)
        follow_button = self.driver.find_element(By.XPATH, '//*[@id="ember26"]/div[2]/div[1]/div[3]/div[1]/div[1]/button')

        # follow_button = self.driver.find_element(By.CLASS_NAME, 'follow   org-company-follow-button org-top-card-primary-actions__action artdeco-button artdeco-button--primary')
        follow_button.click()
        print(f"follow button ={follow_button}")
        
        self.driver.back()
        time.sleep(2.5)
