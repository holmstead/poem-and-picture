# Poem of the day with a random image

This app displays a new poem each day, along with a randomly selected photo/image from your collection of images in the /images directory. The application is witten in python using kivy. The poem of the day is scrapped from: http://www.poems.com/todays-poem/

Requirements:

    1. Python 3.x

    2. kivy

    3. bs4 (BeautifulSoup)

    4. urllib.request 

Instructions:

Put numbered photos in jpg format into images directory as follows:

    1.jpg
    
    2.jpg
    
    3.jpg 	... etc


Kivy is cross-platform, app should work on Android/iOS (not tested on iOS).

The app can be packaged for Android using buildozer, an example init file is provided.
