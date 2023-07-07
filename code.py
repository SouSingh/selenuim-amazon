import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
product_df = pd.DataFrame(columns=['ProductName'])
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("bags")

driver.find_element(By.ID, "nav-search-submit-button").click()


product_name = []
product_url = []
product_price = []
product_rating = []
product_rev = []

name = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
price = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]') 
rating = driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
review = driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]')
elements = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
url_list = [element.get_attribute('href') for element in elements]
for name in name:
  product_name.append(name.text)
for price in price:
  product_price.append(price.text[:24])
for rating in rating:  
  product_rating.append(rating.text)
for review in review:
  product_rev.append(review.text)
for link in url_list:
    product_url.append(link)

print(len(product_name))
print(len(product_price))
print(len(product_rating))
print(len(product_rev))
print(len(product_url))
driver.quit()

data = {
    'Name': product_name,
    'URL': product_url[:24],
    'Price': product_price[:24],
    'Rating': product_rating[:24],
    'Review': product_rev[:24]
}

df = pd.DataFrame(data)
output_path = 'Scrapped_product.xlsx'
df.to_excel(output_path, index=False)
print(df)

