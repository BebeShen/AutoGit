import sys
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = "D:/AutoGitProject/"

# Open chrome
# 1. chrome exe with path self-defined
#
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# Options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# webdriver_path = 'D:\Auto\chromedriver.exe'
# options = Options()

# driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
# 2. default chrome
#
browser = webdriver.Chrome()
browser.get("https://github.com/login")


def create():

    # get project Name & create Project Folder :
    folderName = str(sys.argv[1])
    if not os.path.isdir(path + folderName):
        os.makedirs(path + folderName)
    # account & psw
    element = browser.find_element_by_xpath('//*[@id="login_field"]')
    element.send_keys('BebeShen')
    element = browser.find_element_by_xpath('//*[@id="password"]')
    psw = <Your psw >
    element.send_keys(psw)

    # submit:
    # 1. directly submit
    element.submit()
    # 2. find submit button & click
    # element = driver.find_elements_by_xpath(
    #     '//*[@id="login"]/form/div[4]/input[9]')[0]
    # element.click()

    # create new git project
    browser.get("https://github.com/new")
    element = browser.find_element_by_xpath('//*[@name="repository[name]"]')
    element.send_keys(folderName)
    element.submit()
    browser.quit()

    addgit(folderName=folderName)


def addgit(folderName):
    # chdir to project folder
    folderPath = "D:\AutoGitProject\\" + folderName
    os.chdir(folderPath)
    # print(os.getcwd()) # pwd command

    os.system("git init")
    GitAccount = "BebeShen"
    os.system("git remote add origin https://github.com/" +
              GitAccount + "/" + folderName + ".git")
    # "touch README.md" in windows
    os.system("echo.> README.md")
    os.system("git add .")
    os.system('git commit -m "initial commit"')
    os.system("git push -u origin master")


if __name__ == "__main__":
    create()
