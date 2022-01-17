from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def main() -> None:
    # Instantiate the service that manages WebDriver and the driver itself
    service = Service(executable_path='driver/chromedriver')
    driver = webdriver.Chrome(service=service)

    # Navigate to the website
    driver.get('https://www.python.org/jobs/')

    # Find a job list web element
    jobs_list = driver.find_element(
        by=By.CLASS_NAME, 
        value='list-recent-jobs.list-row-container.menu'
    )

    # Get list items
    listings = jobs_list.find_elements(by=By.TAG_NAME, value='li')

    # Iterate though list items to explore individual job listings
    for item in listings:
        # Find the HTML element with position name tag
        position_elem = item.find_element(
            by=By.CLASS_NAME, 
            value='listing-company-name'
        )
        # Retrieve the (inner) text of web element
        position_name = position_elem.find_element(
            by=By.TAG_NAME, value='a'
        ).text

        # Print the result to the console
        print('Position: ', position_name)

    # Quit the webdriver
    driver.quit()

if __name__ == '__main__':
    main()