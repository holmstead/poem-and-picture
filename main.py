from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
import random, requests, fileinput
from bs4 import BeautifulSoup
from urllib.request import urlopen

## scrape the website
request = requests.get("http://www.poems.com/poem", headers=None)
soup = BeautifulSoup(request.content, 'html.parser')
#print(soup.prettify())

# Find all links in the HTML
all_links = soup.find_all('a')

# Print all the links
#for link in all_links:
    #print(link.get('href'))

# Check if there is at least 17 links
if len(all_links) >= 70:
    # Print the URL of the 17th link
    print("link: ", all_links[68].get('href'))
else:
    print("Not enough links on the page.")

new_href = all_links[68].get('href')
print("New href ", new_href)
request = requests.get(new_href, headers=None)
soup = BeautifulSoup(request.content, 'html.parser')
#print(soup.prettify())

# print title
#print(soup.find_all('p')[0], '\n')
# print poem
#print(soup.find_all('h2')[0], '\n')
# print author
#print(soup.find_all('p')[1], '\n')

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
    with open(filename, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    cleaned_text = soup.get_text(separator='\n', strip=True)

    with open(filename, 'w') as file:
        file.write(cleaned_text)

clean_markup("poem.txt")

# define the kivy style file
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
		img = str('images/' + str(random.randint(1,4)) +'.jpg')
		return img

class myApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)   # sets background color
        return MyLayout()

if __name__ in ('__main__', '__android__'): 
    myApp().run()
