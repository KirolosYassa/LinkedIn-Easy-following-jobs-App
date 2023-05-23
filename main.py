import os
from dotenv import load_dotenv
from LinkedIn import LinkedIn
import time

user = LinkedIn(url="https://www.linkedin.com/jobs/search/?currentJobId=3602007740&f_AL=true&geoId=102007122&keywords=python%20developer&location=Cairo%2C%20Egypt&refresh=true")


user.signin()
number_of_job_list = user.get_jobs_list()
for i in range(len(number_of_job_list)):
    user.click_specific_job(job_index=i)
    user.save_job()
    user.follow_selected_job_company()


