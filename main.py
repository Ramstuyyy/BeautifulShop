from bs4 import BeautifulSoup
import requests
import time

print("Masukkan Skill yang tidak kamu kuasai")
skill_tidak_dikuasai = input(">")
print(f"Memfilter skill yang tidak dikuasai")
def temukan_pekerjaanmu():
    html_req = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_req,'lxml')
    jobs = soup.find_all(name='li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
            diupload = job.find('span', class_ = 'sim-posted').span.text.replace(' ', '')
            #filter kata few di upload
            if 'few' in diupload:
                nama_perusahaan = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
                link_info = job.header.h2.a['href']
                if skill_tidak_dikuasai not in skills:
                    print(f"Nama Perusahaan: {nama_perusahaan.strip()}")
                    print(f"Skill yang dibutuhkan: {skills.strip()}")
                    print(f"Diupload pada: {diupload.strip()}")
                    print(f"Linknya: {link_info.strip()}")

                    print('')

if __name__ == '__main__':
    while True:
        temukan_pekerjaanmu()
        time.wait = 10
        print(f"Menunggu {time.wait} menit...")
        time.sleep(time.wait * 60)