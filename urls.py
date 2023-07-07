import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome()
'''driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("bags")

driver.find_element(By.ID, "nav-search-submit-button").click()


elements = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
url_list = [element.get_attribute('href') for element in elements]
'''

page_urls = [
    'https://www.amazon.in/s?k=bags&sprefix=%2Caps%2C58&ref=nb_sb_ss_recent_1_0_recent',
    'https://www.amazon.in/s?k=bags&page=2&qid=1688700229&sprefix=%2Caps%2C58&ref=sr_pg_1',
    'https://www.amazon.in/s?k=bags&page=3&qid=1688700252&sprefix=%2Caps%2C58&ref=sr_pg_2',
    'https://www.amazon.in/s?k=bags&page=4&qid=1688700270&sprefix=%2Caps%2C58&ref=sr_pg_4',
    'https://www.amazon.in/s?k=bags&page=5&qid=1688701325&sprefix=%2Caps%2C58&ref=sr_pg_5',
    'https://www.amazon.in/s?k=bags&page=6&qid=1688701328&sprefix=%2Caps%2C58&ref=sr_pg_6',
    'https://www.amazon.in/s?k=bags&page=7&qid=1688701488&sprefix=%2Caps%2C58&ref=sr_pg_7'
]
product_url = []
for url in page_urls:
    driver.get(url)
    elements = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    url_list = [element.get_attribute('href') for element in elements]
    for item in url_list:
        product_url.append(item)




df = pd.DataFrame({'URL': product_url})
output_path = 'new_product.csv'  # Replace with the desired output file path
df.to_csv(output_path, index=False)


