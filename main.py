import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    url = "https://www.tff.org/default.aspx?pageID=198"

    response = requests.get(url)
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    score_table = soup.find(class_="s-table")
    team_score = score_table.find_all("tr")
    count= 0
    for count in range(1,20):
        if count < 10:
            print(driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lnkTakim").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lblOyun").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label4").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lblKazanma").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_lblPuan").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label1").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label2").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label5").text +
                  " " + driver.find_element(By.ID,"ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl0"+ str(count) + "_Label3").text)
        else:
            print(driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_lnkTakim").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_lblOyun").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_Label4").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_lblKazanma").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_lblPuan").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_Label1").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_Label2").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_Label5").text +
                  " " + driver.find_element(By.ID, "ctl00_MPane_m_198_10561_ctnr_m_198_10561_grvACetvel_ctl" + str(
                count) + "_Label3").text)

    driver.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
