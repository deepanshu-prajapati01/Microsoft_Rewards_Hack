import os, random, webbrowser, json, start_searches, datetime, time, cv2, pyautogui
import numpy as np
#automate the browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# Initialise the json things
# with open('accounts.json', 'r') as f:
#     DATA = json.load(f)

def getenv(var):
    return os.environ.get(var)
# read from the file
# github_username = getenv('github_username')
# github_password = getenv('github_password')




# Sample DATA
# username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 'XPATHOFTHEPART')))
# username_input.send_keys(sampleData)
# password_xpath = 'xpath'
# password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, passowrd_xpath)))
# password_input.send_keys(sampleData)


class MicrosoftRewardsHack:
    def __init__(self, username : str, password:str, email:str, emailPassword:str) -> None:
        username = self.username
        password = self.password
        email = self.email
        emailPassword = self.emailPassword


    def launchDriver(self):  
        global driver      
        chrome_options = Options()
        chrome_options.add_argument('--incognito')
        chrome_options.add_experimental_option('detach', True)
        # Initialize the WebDriver with the options
        driver = webdriver.Chrome(options=chrome_options)    
        return driver    
    
    
    def interactElement(self, is_text = True, file_path = "temp_target.png"):
        if self.is_text == True:
            screen_image = cv2.imread("screenshot.png", 0)
            # Perform template matching
            result = cv2.matchTemplate(screen_image, file_path, cv2.TM_CCOEFF_NORMED)
            # Set a threshold for matching - it is percentage
            threshold = 0.8
            loc = np.where(result >= threshold)
            # Get the coordinates of the matched region
            points = list(zip(*loc[::-1]))  # Switch x and y coordinates
            if points:
                # Sort points by x coordinate (leftmost point first)
                points = sorted(points, key=lambda x: x[0])
                # Take the first (leftmost) point
                leftmost_point = points[0]
                # Perform the click on the leftmost point
                pyautogui.click(leftmost_point)
                print(f"Clicked at {leftmost_point}")
                return True
            else:
                print("No match found with the given threshold.")
                return False
        
        

    def loginAccount(self, username:str, password:str, email:str, emailPassword:str):
        driver = MicrosoftRewardsHack.launchDriver()
        # loading all data from the file
        with open('loginXpath.json', 'r') as f:
            data = json.load(f)
        
        # Now using the script
        # login here
        
        #email-or-username part
        email_or_username = data["email-or-UsernameInput"]
        id = email_or_username["id"]
        fullXpath = email_or_username["fullXpath"]
        
        currentElement = "Username for Login"
        timeStart = time.time()
        while True:
            try:
                # This try segment tries to catch that particular element!
                try:
                    username_input = WebDriverWait(driver, 10).until(EC.visibility_of_elements_located((By.ID, id)))
                    break
                except TimeoutError:
                    try:
                        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, fullXpath)))
                        break
                    except TimeoutError:
                        currentTime = time.time()
                        if ((currentTime-timeStart)/60) <= 2.3:
                            print(f"Error in finding the element -> [{currentElement}], please take a look at the code")
                            input("Hit enter after the problem is solved!")
                            choice = input("Do you want to start everything from the beginning? (y/n)").lower()
                            if choice == "y":
                                pass
                            elif choice == "n":
                                pass
                            else:
                                pass
                        continue
            except Exception as err:
                #this segment deals with the very rare uncertain things! 100% the code won't come here!
                print("Very complicated issue")
                print(err)
                exit(-2)

        # Now the Username is found, so send the username
        file_path = "temp_target"
        while True:
            try:
                username_input.screenshot_as_png(file_path)
                output = MicrosoftRewardsHack.interactElement(file_path=f"{file_path}.png")
                if output == True:
                    pyautogui.typewrite(username, interval=0.2)
                    break
                elif output == False:
                    continue
            except Exception as err:
                print(f"Error occure -> {err}")
        
        



        #email-or-UsernameNextButton part
        email_or_UsernameNextButton = data["email-or-UsernameNextButton"]
        id = email_or_UsernameNextButton["id"]
        fullXpath = email_or_UsernameNextButton["fullXpath"]

        currentElement = "Username Next Button"
        timeStart = time.time()
        while True:
            try:
                # This try segment tries to catch that particular element!
                try:
                    username_next_button = WebDriverWait(driver, 10).until(EC.visibility_of_elements_located((By.ID, id)))
                    break
                except TimeoutError:
                    try:
                        username_next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, fullXpath)))
                        break
                    except TimeoutError:
                        currentTime = time.time()
                        if ((currentTime-timeStart)/60) <= 2.3:
                            print(f"Error in finding the element -> [{currentElement}], please take a look at the code")
                            input("Hit enter after the problem is solved!")
                            choice = input("Do you want to start everything from the beginning? (y/n)").lower()
                            if choice == "y":
                                pass
                            elif choice == "n":
                                pass
                            else:
                                pass
                        continue
            except Exception as err:
                #this segment deals with the very rare uncertain things! 100% the code won't come here!
                print("Very complicated issue")
                print(err)
                exit(-2)




        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 'XPATHOFTHEPART')))
        username_input.send_keys("sampleData")
        
        
        
if __name__ == '__main__':
    MicrosoftRewardsHack.loginAccount(username="temp", password="sfs", email="sdf", emailPassword="Sdf")