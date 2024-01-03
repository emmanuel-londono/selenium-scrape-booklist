from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

# Web Driver Settings
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(10)
base_url = "https://www.thegreatestbooks.org/page/"
output_file="greatest_books_of_all_time_list.txt"

def scrape_books(base_url,output_file):
    try:
        for number in range(1, 224):
            print(f'///////Page Number {number}/////////')
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

            with open(output_file, "a", encoding='utf-8') as file:
                for element in all_elements:
                    file.write(element.text + "\n")
    except WebDriverException as e:
        print(f"An error occurred: {e}")

    finally:
        # End Session
        print("Scrape Completed!")
        driver.quit()

scrape_books(base_url, output_file)