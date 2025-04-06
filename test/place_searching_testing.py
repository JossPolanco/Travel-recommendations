from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def initializeDriver():
    driver = webdriver.Edge()
    return driver

def main():
    driver = initializeDriver()
    driver.get("http://127.0.0.1:9000/")
    driver = search_place(driver)


def search_place(driver):
    # Gets all the inputs of the form
    input_origin =  driver.find_element(By.ID, "origin")
    input_destiny = driver.find_element(By.ID, "place")
    input_distance = driver.find_element(By.ID, "distance")
    input_budget = driver.find_element(By.ID, "budget")
    btn_search = driver.find_element(By.CLASS_NAME, "search_btn")
    # paths of dropdowns
    weather_dropdown = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div[1]/div/input")
    season_dropdown = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div[2]/div/input")
    # path of dropdown's options
    weather_option = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div[1]/div/ul/li[9]/span")
    season_option = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div[2]/div/ul/li[2]/span")
    

    
    # Sets the data to the inputs and selects
    time.sleep(2)
    input_origin.send_keys("Chihuahua")
    time.sleep(2)
    input_destiny.send_keys("Playa")
    time.sleep(2)
    input_distance.send_keys("50000")
    time.sleep(2)
    input_budget.send_keys("50000")
    time.sleep(2)
    weather_dropdown.click()
    time.sleep(1)
    weather_option.click()
    time.sleep(2)
    season_dropdown.click()
    time.sleep(1)
    season_option.click()
    time.sleep(2)
    btn_search.click()
    time.sleep(5)
    
    place_seeMore = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div[3]/a")
    place_seeMore.click()
    time.sleep(20)
    

if __name__ == "__main__":
    main()