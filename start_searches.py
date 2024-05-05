import cv2
import numpy as np
import pyautogui
from matplotlib import pyplot as plt
import time, os
import random, requests



def getSearchQueries(num: int, api_url: str, api_key: str) -> list:
    # List to store the final search queries
    search_queries = []
    # Fetch and store the search queries
    for _ in range(num):
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()
            # Assuming 'Login' is the key for search queries
            search_queries.append(data[api_key])
        except requests.RequestException as e:
            print(f'An error occurred: {e}')
            return False
    # Return the list of search queries
    print(search_queries)
    return search_queries


def searchQueries(num: int) -> list:
    search_queries = []
    APIs = {
            "activity": "https://www.boredapi.com/api/activity",
            "setup" : "https://official-joke-api.appspot.com/random_joke",
            "punchline" : "https://official-joke-api.appspot.com/random_joke"
            }
    
    # for api in APIs:
    #     print(api, APIs[api])

    for api in APIs:
        try:
            search_queries = getSearchQueries(num=num, api_url=APIs[api], api_key=api)
            if type(search_queries) == list:
                break
            continue
        except:
            pass
        
    if search_queries == []:
        search_queries = False
    return search_queries



def interact(path="./target.jpg", percentage=0.4):
    try:
        # Read the target image as a grayscale image
        target_image = cv2.imread(path, 0)
        if target_image is None:
            raise ValueError(f"Image at path {path} could not be read.")
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        screen_image = cv2.imread("screenshot.png", 0)
        # Perform template matching
        result = cv2.matchTemplate(screen_image, target_image, cv2.TM_CCOEFF_NORMED)
        # Set a threshold for matching
        threshold = percentage
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
    except Exception as err:
        print(err)
        exit(-1)


def preInteract(percentage:int) -> bool:
    targets = os.listdir()
    if "screenshot.png" in targets:
        targets.remove("screenshot.png")
    print(targets)
    for target in targets:
        if interact(path=target, percentage=percentage) == False:
            continue
        else:
            return True
    return False


def main(searches = 10, percentage=0.4):
    os.chdir("targets")
    search_queries = searchQueries(num=searches)
    for search_query in search_queries:
        time.sleep(random.uniform(0.6, 2))
        if preInteract(percentage=percentage):
            '''if it returns false then the program will not work and stops immediately'''
            time.sleep(random.uniform(0.6, 2))
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            time.sleep(random.uniform(0.6, 2))
            pyautogui.typewrite(" h\b", interval=0.1)
            pyautogui.typewrite(search_query, interval=0.1)
            time.sleep(random.uniform(0.6, 2))
            pyautogui.press("enter")
            time.sleep(3)
    os.chdir("..")


if __name__ == '__main__':
    pass
    # main(searches=int(input("Enter the amount of searches you want (max-30)")), percentage=0.5)
