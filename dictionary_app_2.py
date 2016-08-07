import requests
from bs4 import BeautifulSoup

print('Welcome to online Dictionay App 2.\n\nEnter any word to get its meaning and definition.\nYou can also search by entering multiple words, seperated by a "comma(,)"\n\nEnter "q" to quit.\n')

while True:
	try:
		
		url = "http://www.synonym.com/synonym/"
		word = input("Enter your word: ")
		url = url + word
		
		if word == 'q':
			break
			
		else:
		
			data = requests.get(url)
			soup = BeautifulSoup(data.text, 'html.parser')
			data1 = soup.find_all('div', {'class':'synonym'})

			for i in data1:
				print(i.contents[1].text)
			
	except NameError:
		print('Sorry, the word you entered does not exits.')
		
	except:
		print('Something went wrong, please try again.')