import requests
import urllib3
from bs4 import *
import configparser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Rdsdb():

    def __init__(self, user, password):
        url_login = 'https://rdsdb.rcs-rds.ro/admin/auth/login'
        data = {'username': user, 'password': password, 'login': 'Login'}
        self.sesiune = requests.Session()
        # request pentru logare, obtine cookies
        self.sesiune.post(url_login, data=data, verify=False)

    def get_final_url(self):
        configfile = configparser.ConfigParser()
        configfile.read('config.ini')
        urls = dict(configfile.items('URLS'))
        # primul request catre pagina de tickete, care returneaza un lnk de redirect, stocat mai tarziu in url_redirect
        req1 = self.sesiune.get(urls['url_tickete_grup'], verify=False)
        soup_req1 = BeautifulSoup(req1.text, 'html.parser')
        url_redirect = soup_req1.a['href']
        req2 = self.sesiune.get(url_redirect, verify=False)
        soup_req2 = BeautifulSoup(req2.text, 'html.parser')
        for tag in soup_req2.findAll('meta'):
            if "https" in tag['content']:
                redirect_to_tks = tag['content'].split("'")[1]
        return redirect_to_tks

    def getsession(self):
        return self.sesiune
