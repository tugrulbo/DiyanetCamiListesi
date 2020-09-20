from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


def veriCek():
    mosqueList={"id":0,"city":"","state":"","mosques":{
        "id":0,
        "name":"",
        "address":""
    }}
    i = 2
    j= 2
    k=1
    cityCounter = 0
    mosqueCounter =0
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://camiler.diyanet.gov.tr")
    time.sleep(3)
    citySelect = driver.find_element_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIl"]').click()
    time.sleep(2)
    cityCount = len(driver.find_elements_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIl"]/option'))
    while(i<cityCount):
        citySelected = driver.find_element_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIl"]/option[{0}]'.format(i)).click()
        cityName = driver.find_element_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIl"]/option[{0}]'.format(i)).text
        time.sleep(2)
        stateSelect = driver.find_element_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIlce"]').click()
        time.sleep(2)
        stateCount = len(driver.find_elements_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIlce"]/option'))
        while(j<stateCount):
            stateSelected = driver.find_element_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIlce"]/option[{0}]'.format(j)).click()
            stateName = driver.find_element_by_xpath('//*[@id="ctl00_ctl35_g_7c8222a9_e27f_4831_b393_65197bc417d3_drpIlce"]/option[{0}]'.format(j)).text
            time.sleep(2)
            mosqueStateCount = len(driver.find_elements_by_xpath('//*[@id="DataTable"]/tbody/tr'))
            time.sleep(2)
            while(k < mosqueStateCount):
                l=1
                mosqueName = driver.find_element_by_xpath('//*[@id="DataTable"]/tbody/tr[{0}]/td[{1}]'.format(k,l)).text
                l += 1
                mosqueAddres = driver.find_element_by_xpath('//*[@id="DataTable"]/tbody/tr[{0}]/td[{1}]'.format(k,l)).text
                mosqueList.update({"id":cityCounter,"city":cityName,"state":stateName,"mosques":{
                                        "id":mosqueCounter,
                                        "name":mosqueName,
                                        "address":mosqueAddres
                                 }})
                print("ID:{0} --- City Name:{1} --- State Name:{2} --- ID:{3} --- Name:{4} -- Address:{5}".format(cityCounter,cityName,stateName,mosqueCounter,mosqueName,mosqueAddres))
                mosqueCounter += 1
                l=1
                k += 1
            time.sleep(1)
            j += 1
            k=1
            mosqueCounter=0
        i += 1
        cityCounter += 1
        j=2
        

    driver.close()
    print(mosqueList)
    with open("output.json",w) as f:
        f.write(mosqueList)
veriCek()
