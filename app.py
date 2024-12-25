from bs4 import  BeautifulSoup
import requests
import random
import string

from utiles import * 



class TelegramDevApi:
    
    def __init__(self, PHONE):
        self.PHONE = PHONE
        
        # Status 
        self.is_connect     = False
    
    
    def _api_v1(self, path: str, headers : dict, data :dict = None):
        response = requests.post(
            url=f'https://my.telegram.org{path}', 
            headers=headers, data=data
        )
        return response
    
    
    def _api_v2(self, path: str, headers : dict):
        response = requests.post(
            url=f'https://my.telegram.org{path}', 
            headers=headers
        )
        return response
    
    
    def SEND_CODE(self,):
        data = self._api_v1('/auth/send_password', headers=SEND_CODE_HEADERS, data={'phone':self.PHONE})
        if 'Sorry, too many tries. Please try again later' in data.text:
            raise ManyTries(f'Sorry, too many tries. Please try again later')
        self.random_hash = data.json()['random_hash']
        return True

    def LOGIN(self, code : str):
        if self.is_connect:
            raise Exception('Client Is Login ')
        data = self._api_v1('/auth/login', headers=SEND_CODE_HEADERS, data={
            'phone':self.PHONE, 'random_hash':self.random_hash, 'password':code
        })
        if 'Invalid confirmation code!' in data.text:
            raise CodeInvalid('Invalid confirmation code!')
        
        if data.text != "true":
            raise Exception('Unknown error, tra agin .')
        
        self.token = data.headers['Set-Cookie']
        self.APP_HEADERS = APP_AUTH_HEADERS
        self.APP_HEADERS['Cookie'] =  self.token 
        return True
    
    def CHECK_APP_CREATE(self, data):
        soup = BeautifulSoup(data.text, 'lxml')
        return bool(soup.find_all('span', {'class':'form-control input-xlarge uneditable-input','onclick':'this.select();'}))
    
    def GET_API(self):
        data = self._api_v2("/apps", headers=self.APP_HEADERS)
        if not self.CHECK_APP_CREATE(data):
            status = self.CREAT_APP(data)
            if not status:
                raise Exception('App Create Error .')
            data = self._api_v2("/apps", headers=self.APP_HEADERS)
        api_id, api_hash = self.SCRIP_DATA(data)
        return api_id, api_hash
        
    
    def SCRIP_DATA(self, data):
        soup = BeautifulSoup(data.text, 'lxml')
        apis = soup.find_all('span', {'class':'form-control input-xlarge uneditable-input','onclick':'this.select();'})
        return apis[0].text, apis[1].text
    
    def CREAT_APP(self, data):
        print('create app ')
        CREATE_APP_HED = CREATE_APP_HEADERS
        CREATE_APP_HED['Cookie'] = self.token
        hashs = BeautifulSoup(data.content, 'lxml').find('input', {'name': 'hash'})['value']
        print(hashs)
        data_ = {
            'hash': hashs,
            'app_title': self.GENRATE_WORDS(),
            'app_shortname': self.GENRATE_WORDS(),
            'app_url': 'www.telegram.org',
            'app_platform': 'other',
            'app_desc': self.GENRATE_DESCRIPTION()
          }
        response = self._api_v1('/apps/create', headers=CREATE_APP_HED, data=data_)   
        if response.status_code == 200:
            return True
        else : return False
        
    def GENRATE_WORDS(self):
        word = ""
        for i in range(random.randint(5,9)):
            word += random.choice(string.ascii_lowercase)
        return word
    
    def GENRATE_DESCRIPTION(self):
        sentence = "".join([])
        for i in range(random.randint(5,9)):
            sentence += self.GENRATE_WORDS() + " "
        return sentence
    
    
    
apps = TelegramDevApi('+212 78 175 8888')
apps.SEND_CODE()
apps.LOGIN(input(' code >'))
data = apps.GET_API()
print(data) # 