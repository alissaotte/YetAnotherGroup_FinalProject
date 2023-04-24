##################################################################################################################
# Names: Brant Kightlinger, Alissa Otte, Erik Sibri
# Emails: kightlbc@mail.uc.edu, otteal@mail.uc.edu, sibriee@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010 002
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that we are able to collaborate as a group to find our team's location.
#   (cont.) This module is our function where we load in our JPG image with us at our location and then show the image
# Citations: https://www.geeksforgeeks.org/python-pil-image-show-method/#
# Anything else that's relevant: N/A
##################################################################################################################

from PIL import Image

def loadPicture():
    f = "YetAnotherGroup_Crosley_Picture.jpg" # REPLACE THIS WITH OUR IMAGE
    img = Image.open(f)
    return img.show()
    # https://www.geeksforgeeks.org/python-pil-image-show-method/#