import requests
import urllib3
from bs4 import *
import configparser


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Rdsdb():
    opt_cfg = configparser.ConfigParser()
    opt_cfg.read('config.ini')
    queue = dict(opt_cfg.items('OPTIONS'))

    urls_file = configparser.ConfigParser()
    urls_file.read('urls.ini')
    urls = dict(urls_file.items('URLS'))

    cod = ''

    def __init__(self, user, password):

        data = {'username': user, 'password': password, 'login': 'Login'}
        self.sesiune = requests.Session()
        # request pentru logare, obtine cookies si cod instalator
        req = self.sesiune.post(self.urls['url_login'], data=data, verify=False)
        soup_req = BeautifulSoup(req.text, 'html.parser')
        self.cod = soup_req.find('span', {'id': 'userId'})
        self.cod = self.cod.contents[0]

    def get_final_url(self):

        # primul request catre pagina de tickete, care returneaza un lnk de redirect, stocat mai tarziu in url_redirect
        if self.queue['queue'] == 'user':
            req1 = self.sesiune.get(self.urls['url_tickete_user1'] + self.cod + self.urls['url_tickete_user2'], verify=False)
        elif self.queue['queue'] == 'group' :
            req1 = self.sesiune.get(self.urls['url_tickete_grup'], verify=False)
        else:
            return 20

        soup_req1 = BeautifulSoup(req1.text, 'html.parser')
        url_redirect = soup_req1.a['href']

        req2 = self.sesiune.get(url_redirect, verify=False)
        soup_req2 = BeautifulSoup(req2.text, 'html.parser')
        for tag in soup_req2.findAll('meta'):
            if "https" in tag['content']:
                redirect_to_tks = tag['content'].split("'")[1]

        if redirect_to_tks == 'https://rdsdb.rcs-rds.ro/admin/auth/logout':
            return 10
        else:
            return redirect_to_tks

    def getsession(self):
        return self.sesiune
