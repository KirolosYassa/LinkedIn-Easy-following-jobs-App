import os
from dotenv import load_dotenv
from LinkedIn import LinkedIn
import time

user = LinkedIn(url="https://www.linkedin.com/jobs/search/?currentJobId=3602007740&f_AL=true&geoId=102007122&keywords=python%20developer&location=Cairo%2C%20Egypt&refresh=true")


user.signin()
job_list = user.get_jobs_list()

print("----------------------------------------------------")
for i in range(len(job_list)):
    print(f"company = {job_list[i].text}")
    user.click_specific_job(job_index=i)
    user.save_job()
    user.follow_selected_job_company()
    print("----------------------------------------------------")

