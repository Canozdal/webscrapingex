import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def scrapeData(url,driver, arr):

    driver.get(url)
    no_teams = 20
    count= 0
    for count in range(1,no_teams):
        if count < 10:
            team = {"name" : driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lnkTakim").text,
                    "played": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lblOyun").text,
                    "won": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label4").text,
                    "tie": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lblKazanma").text,
                    "loss": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lblPuan").text,
                    "scored_goals": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label1").text,
                    "yedigi" : driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label2").text,
                    "points" : driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label3").text
                    }
        else:
            team = {"name" : driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_lnkTakim").text,
                    "played": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_lblOyun").text,
                    "won": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_Label4").text,
                    "tie": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_lblKazanma").text,
                    "loss": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_lblPuan").text,
                    "scored_goals": driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_Label1").text,
                    "yedigi" : driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_Label2").text,
                    "points" : driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl"+ str(count) + "_Label3").text
                    }
        arr.append(team)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url = "https://www.tff.org/default.aspx?pageID=198"

    driver = webdriver.Chrome()
    arr = []
    scrapeData(url,driver,arr)

    print(arr[0])
    driver.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
