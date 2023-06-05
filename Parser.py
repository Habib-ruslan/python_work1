from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://omgtu.ru/general_information/faculties/'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    faculty_list = soup.select('div#pagecontent ul li a')
    faculty_names = []
    for faculty in faculty_list:
        faculty_names.append(faculty.get_text(strip=True))
    save_result_in_file(faculty_names)


def save_result_in_file(faculty_names):
    with open('faculty_names.txt', 'w') as file:
        for name in faculty_names:
            file.write(name + '\n')
    file.close()
