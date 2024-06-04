import requests
from bs4 import BeautifulSoup

def fetch_resume(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    resume_content = soup.find('div', class_='resume-content').text
    return resume_content

urls = ["url1", "url2", ...]  # List of URLs
resumes = [fetch_resume(url) for url in urls]

# Save resumes to local files
for idx, resume in enumerate(resumes):
    with open(f'resume_{idx}.txt', 'w') as f:
        f.write(resume)
