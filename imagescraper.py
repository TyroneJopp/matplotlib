from PIL import Image
import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Tree'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

image = soup.find('img')
image_url = image['src']


img = Image.open(requests.get(image_url, stream = True).raw)

img.save('image.jpg')