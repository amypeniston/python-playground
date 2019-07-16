import requests
from bs4 import BeautifulSoup
import re

def print_header(source):
    print("------ Fetching Jobs from", source, "------")

def get_rg_jobs_data():
    url = "http://www.royalgazette.com/jobs"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    headers = {"User-Agent": user_agent}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # For testing
    # with open("output.html", "w") as file:
    #     file.write(str(soup.encode("utf-8")))

    jobs_section = soup.find(class_="col-1")
    jobs_header = jobs_section.find("h2")

    print(jobs_header.next_sibling.strip(),'\n')

    jobs_divs = jobs_section.find_all("div", id=False)

    counter = 0
    for job in jobs_divs:
        if counter % 2 == 0:
            job_content = job.text.strip().replace("Read more >>","")
            print(job_content)
        counter = counter + 1

def get_jib_jobs_data():
    url = "http://www.jobsinbda.com/jm-ajax/get_listings/"
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    headers = {"User-Agent": user_agent}

    form_data = {"page": 1, "per_page": 15}

    page = requests.post(url, headers=headers, data=form_data)
    soup = BeautifulSoup(page.content, "html.parser")

    # Search for malformed HTML tag
    jobs = soup.find_all(class_=r'\"position\"')
    str_jobs = str(jobs)

    # Fix malformed h3 tags
    fixed_str_jobs = str_jobs.replace(r'&lt;\/h3&gt;',"</h3>")

    # Seach for text in h3 tags
    titles = re.findall(r'<h3>(.*?)</h3>', fixed_str_jobs)

    for i, title in enumerate(titles):
        print(i, title)

job_sources = {
    "source_names": ["Royal Gazette", "Jobs in Bermuda"],
    "source_functions": [get_rg_jobs_data, get_jib_jobs_data]
}

for i in range(len(job_sources["source_names"])):
    print_header(job_sources["source_names"][i])
    job_sources["source_functions"][i]()