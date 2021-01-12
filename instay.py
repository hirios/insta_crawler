from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = r'PATH FROM CRHOMEDRIVER'
user = 'YOUR USER'
password = 'YOUR PASSWORD'

if len(PATH) == 0:
    PATH = input('Digite o caminho para o "chromedriver.exe": ')
    
if len(user) == 0:
    user = input('Seu USERNAME: ')
    
if len(password) == 0:
    password = input('Sua SENHA: ')


class Insta():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.s = ''
        

    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(3)
        self.driver.find_element_by_name('username').send_keys(user)
        self.driver.find_element_by_name('password').send_keys(password)
        ENTER = 'Igw0E.IwRSH.eGOV_._4EzTm'
        self.driver.find_element_by_class_name(ENTER).click()
        sleep(4)
        

    def get_values(self):
        """ Get total numbers of "followers" and "following """
        
        if self.driver.current_url == 'https://www.instagram.com/' + user + '/':
            self.seguidores = int([x for x in self.driver.page_source.split('"') if 'seguidores' in x][2].split('<')[0].split('>')[-1])
            self.seguindo = int([x for x in self.driver.page_source.split('"') if 'seguindo' in x][2].split('<')[0].split('>')[-1])
        else:
            self.driver.get('https://www.instagram.com/' + user)
            sleep(2)
            self.seguidores = int([x for x in self.driver.page_source.split('"') if 'seguidores' in x][2].split('<')[0].split('>')[-1])
            self.seguindo = int([x for x in self.driver.page_source.split('"') if 'seguindo' in x][2].split('<')[0].split('>')[-1])
            
            
    def focus(self, followers_or_following):
        """ Set focus in the followers window """
        
        self.s = followers_or_following
        self.driver.find_element_by_xpath(f"//a[contains(@href,'{followers_or_following}')]").click()
        sleep(3)
        self.driver.find_element_by_xpath('//body').click()
        self.driver.find_element_by_xpath('//body').send_keys(Keys.END)
        self.driver.find_element_by_xpath('//body').send_keys(Keys.END)
        self.driver.find_element_by_xpath('//body').send_keys(Keys.END)
        self.driver.find_element_by_xpath('//body').click()
        self.driver.find_element_by_xpath('//body').click()


    def number_so_far(self):
        """ Get number of followers scrapped so far """
        
        lista = list(set(self.driver.find_elements_by_class_name('Jv7Aj.mArmR.MqpiF')))
        n = len(lista)
        return n


    def scrool(self):

        if self.s == 'followers':
            self.num = self.seguidores

        elif self.s == 'following':
            self.num = self.seguindo
        
        while self.number_so_far() < self.num:
            print(self.number_so_far(), self.num)
            self.driver.find_element_by_xpath('//body').send_keys(Keys.END)
            sleep(0.2)
            self.driver.find_element_by_xpath('//body').send_keys(Keys.END)
            sleep(0.2)
            self.driver.find_element_by_xpath('//body').send_keys(Keys.END)


    def get_list(self):
        self.lista = list(set(self.driver.find_elements_by_class_name('Jv7Aj.mArmR.MqpiF')))
        return self.lista


def lista_seguindo():
    insta.get_values()
    insta.focus('following')
    insta.scrool()
    lista = insta.get_list()
    return lista


def lista_seguidores():
    insta.get_values()
    insta.focus('followers')
    insta.scrool()
    lista = insta.get_list()
    return lista


if __name__ == '__main__':
    insta = Insta()
    insta.login()
    lista1 = lista_seguindo()
    lista2 = lista_seguidores()
