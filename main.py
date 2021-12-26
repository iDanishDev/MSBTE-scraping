import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
 

file = open('e_no.txt','r')

file_result = open('results.txt','w+')




for each in file:


    #Driver Opening the Link 
    driver.get("https://msbte.org.in/DISRESLIVE2021CRSLDSEP/frmALYSUM21PBDisplay.aspx")
    #Keeping a copy of the main window
    main_window = driver.current_window_handle

    #Selecting the <select> and updating its value to 2, To change the mode of Scraping
    select = Select(driver.find_element_by_id("ddlEnrollSeatNo"))
    select.select_by_value("2")

    #Searching the input box
    search = driver.find_element_by_id("txtEnrollSeatNo")

    #Inputting every single keys from the file to the input box and printing them to terminal(for reference)
    search.send_keys(each)
    print(each)
    
    
    #switching window to the 2nd window open and accesing the proper aggregate percentage using xpath and converting web element to text and printing the aggregate percentage to terminal(for reference)
    driver.switch_to.window(driver.window_handles[1])
    try:
        results = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/table/tbody/tr[5]/td[3]/strong").text
        file_result.write(each+results+"\n\n")
        
    except NoSuchElementException:
        print("Skipped Due to Different XPath")
        file_result.write(each+"\nSkipped Due to an External Error"+"\n\n")
        pass
    
    

    #shutting down driver
    driver.quit
    

time.sleep(1)

driver.stop_client