from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
import random, requests, fileinput, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

## scrape the website
request = requests.get("http://www.poems.com/todays-poem/", headers=None)
soup = BeautifulSoup(request.content, 'html.parser')
#print(soup.prettify())

## get body paragraph **with html tags
body = (soup.find_all('p')[0])


def find_tags(tag):
	'''locates given html tags in soup'''
	i=0
	while i == True :
		x = soup.find_all(tag)[i].get_text(" ")
		print(str(i), x)
		i+=1

#find_tags('h2')


## save the scraped poem
with open("poem.txt", 'w') as outf:
	#outf.write(str(title))
	outf.write(str(body))

## parse the poem
def clean_markup(filename):
    '''Removes html tags from text in text file''' 
    with fileinput.FileInput(filename, inplace = True, backup ='.bak') as f:
        for line in f:
            if('<span class="excerpt_line">' in line):
                print(line.replace('<span class="excerpt_line">','\n'), end ='')
            elif('<p>' in line):
                print(line.replace('<p>','\n'), end ='')
            elif('&amp;' in line):
                print(line.replace('&amp;','&'), end ='')
            elif('<em>' in line):
                print(line.replace('<em>',''), end ='')
            elif('</em>' in line):
                print(line.replace('</em>',''), end ='')
            elif('</span>' in line):
                print(line.replace('</span>',''), end ='')
            elif('</p>' in line):
                print(line.replace('</p>',''), end ='')
            else:
                print(line, end ='')

clean_markup("poem.txt")
clean_markup("poem.txt")
clean_markup("poem.txt")
clean_markup("poem.txt")
clean_markup("poem.txt")


Builder.load_file('poem.kv')

class MyLayout(BoxLayout):
	def __init__(self):
		super(MyLayout, self).__init__()
	
	def get_title(self):
		'''reads the title of the poem from the scraped html'''
		title = "\n\n" + str((soup.find_all('h2')[0].get_text(" ")))
		return title
	
	def get_text(self):
		''' reads the poem from the text file'''
		with open("poem.txt","r") as inf:
			return(inf.read())
    
	def get_author(self):
		'''gets author name from soup'''
		author = "\n\n\n\n\n" + str((soup.find_all('p')[1].get_text(" ")))
		return author

	def get_image(self):
		'''
		generates random number and returns a random image path
		for the kivy file to use as source
		'''
		img = str('images/' + str(random.randint(1,len(os.listdir("./images")))) +'.jpg')
		return img


class myApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)   # sets background color
        return MyLayout()


if __name__ in ('__main__', '__android__'): 
    myApp().run()
