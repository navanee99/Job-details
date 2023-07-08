from bs4 import BeautifulSoup

import requests

html_text=requests.get('https://www.simplyhired.co.in/search?q=company+contact+details&l=tamil+nadu&job=5AcDd7UEfQA4DHQ7pbzYYH9JC1WRzv_33wOl5CFL-dMiTDeoEyA6pg').text
soup=BeautifulSoup(html_text,'lxml')
job=soup.find('div',class_='RightPane-spaceKeeper').text
print(f'{job}')