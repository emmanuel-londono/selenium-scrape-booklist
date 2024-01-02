from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = "https://www.thegreatestbooks.org/page/"

for number in range(1, 224):
    url = f"{base_url}{number}"
    driver.get(url)
    
    # Browser Information//
    title = driver.title

    # Web Page Content//
    # Wait for webpage to sync up
    driver.implicitly_wait(1)

    # Establish locators
    all_elements = driver.find_elements(By.XPATH, "//h4/a[contains(@href, '/books/')]")

    for element in all_elements:
        print(element.text)

    # Write elements to file output

    with open("greatest_books_of_all_time_list.txt", "a") as file:
        for element in all_elements:
            file.write(element.text + "\n")


# End Session
driver.quit()
