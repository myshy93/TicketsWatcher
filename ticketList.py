import connections
from bs4 import *
import configparser


class Tickets:

    def __init__(self):
        configfile = configparser.ConfigParser()
        configfile.read('config.ini')
        login_data = dict(configfile.items('LOGIN'))
        self.connect = connections.Rdsdb(login_data['user'], login_data['pass'])
        self.url = self.connect.get_final_url()
        self.sesiune = self.connect.getsession()

    def pull_tickets(self):
        self.raw_tickets_array = []
        req = self.sesiune.get(self.url, verify=False)
        soup_tk = BeautifulSoup(req.text, 'html.parser')

        for tag in soup_tk.findAll('tr'):
            if tag.findAll('script'):
                for tag_script in tag.findAll('script'):
                    for x in tag_script:
                        self.raw_tickets_array.append(x)

    def get_raw_tickets_list(self):
        return self.raw_tickets_array

    def get_tks_ids_list(self):
        tks_id_list = list()
        for tk in self.raw_tickets_array:
            tks_id_list.append(tk.split("'")[1])
        return tks_id_list


