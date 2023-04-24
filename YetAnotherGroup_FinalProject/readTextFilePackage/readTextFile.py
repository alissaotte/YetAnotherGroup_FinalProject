##################################################################################################################
# Names: Brant Kightlinger, Alissa Otte, Erik Sibri
# Emails: kightlbc@mail.uc.edu, otteal@mail.uc.edu, sibriee@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010 002
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that we are able to collaborate as a group to find our team's location.
#   (cont.) This module is our function where we extract the JSON, load the text file as a list, and then used list
#   (cont.) comprehension to find our location's riddle.
# Citations: https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
#   (cont.) https://www.geeksforgeeks.org/read-json-file-using-python/#
#   (cont.) https://www.w3schools.com/python/python_lists_comprehension.asp
# Anything else that's relevant: N/A
##################################################################################################################

import json

def findOurLocation():
    #### OPENING TEXT FILE ####
    with open('english.txt', 'r') as f:
        # Use splitlines() so that the /n doesn't show up
        textFileList = f.read().splitlines()
    # print(textFileList) # debugging to make sure the list looks good
    # https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
    
    #### READING JSON FILE ####
    # opening JSON file
    f = open('EncryptedGroupHints Spring 2023 Section 002.json')
    # returns JSON object as a dictionary
    data = json.load(f)
    # iterating through the json list
    locationsHintsList = []
    for i in data['Yet Another Group']:
        locationsHintsList.append(i)
    # Closing file
    f.close()
    print("This are our hint numbers: ", locationsHintsList)
    # https://www.geeksforgeeks.org/read-json-file-using-python/#
    
    #### FINDING LOCATION ####
    locationAnswer = []
    # List comprehension to iterate through hint numbers list and lookup those values in the text file list
    for x in locationsHintsList:
        # Using -1 to account that the list starts at 0 vs the text file starts at 1
        x = int(x) - 1
        locationAnswer.append(textFileList[x])
    print("This is our location riddle: ", locationAnswer)
    print("Therefore, our location was: Crosley Tower")
    # https://www.w3schools.com/python/python_lists_comprehension.asp