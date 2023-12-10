import requests
from bs4 import BeautifulSoup

print('Video games on Bol.com that cost between €100 and €500:')

# Create loop to iterate over multiple pages (first 20)
for i in range(1, 21):

    # Scrape content from web page
    url = f'https://www.bol.com/nl/nl/l/videogames/18200/?page={i}'
    response = requests.get(url)
    content = response.content

    # Find specific content based on div class
    soup = BeautifulSoup(content, 'html.parser')
    products = soup.find_all('div', class_='product-item__content')

    # Loop over product details and add data to the list (if the info exists) -- filter on price
    for product in products:

        product_price = 0
        promo_price = product.find('span', class_='promo-price')
        if promo_price:
            product_price = int(promo_price.text.split()[0])
            if 100 <= product_price < 500:

                product_owner = product.find('ul', class_='product-creator').text.replace('\n\n', '')

                product_name = 'None'
                product_title = product.find('a', class_='product-title')
                if product_title:
                    product_name = product_title.text

                rating = 0
                product_review = product.find('div', class_='star-rating')
                if product_review:
                    rating = int(product_review.span['style'].replace('width: ', '').replace('%', ''))
                    rating = rating / 10

                print(f''''
                Company: {product_owner}
                Product: {product_name}
                Price: €{product_price}
                Rating: {rating}/10.0
                ''')
