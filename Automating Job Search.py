from bs4 import BeautifulSoup
import requests
import time

print('Put a skill that you are not familiar with')
unfamiliar_skill = input('>').split()
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, features="lxml")
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'today' or '1 day' or 'few days' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ","")
            skills = job.find('span', class_='srp-skills').text.replace(" ","")
            moreInfo = job.header.h2.a['href']
            have_unfamiliar_skill = True
            for skill in unfamiliar_skill:
                if skill in skills:
                    have_unfamiliar_skill = False
                    break

            if have_unfamiliar_skill == True:
                with open(f'Job Details/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n")
                    f.write(f"More Info : {moreInfo.strip()}") 
                print(f'File saved: {index}')

if __name__=='__main__':
    find_jobs()
