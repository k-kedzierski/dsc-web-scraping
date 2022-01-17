# 1-first-script

First part of Data Science Club introductory web scraping course.

In this part, you'll learn the basics of web scraping with Selenium in Python, and write your very first script.

# Before you start

In the repository, a new directory has been created, named `driver`. **Place the previously downloaded WebDriver here.**

For the sake of clarity, in all of the examples the WebDriver will be initialized from this folder.

After this, your directory should look similar to the structure presented below. Note that the name of the file **does not have to match**, and will vary depending on the browser of choice.

```
├── README.md
├── driver
│   └── chromedriver
```

* ⚠️ If working on Unix-like system, remember to make sure that proper access permissions are set for the WebDriver file (`chmod`).

# First script

Consider a following website: https://www.python.org/jobs/:

![](https://i.imgur.com/vldHYwK.png)

It is a subsite of the official Python website, which contains job listings. In this first example, you'll learn how, using Selenium, to **visit the website** and **get the job position names** from job listings.

## Contents

Contents of the [first-script.py](first-script.py):

---

<details>
  <summary>👉 Click to expand!</summary>
  
  ```python
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
          position_name = position_elem.find_element(by=By.TAG_NAME, value='a').text

          # Print the result to the console
          print('Position: ', position_name)

      # Quit the webdriver
      driver.quit()

  if __name__ == '__main__':
      main()
  ```
</details>

---

## Walkthrough

### Importing modules

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
```

Selenium handles web browser though WebDrivers, which can be easily imported from `selenium.webdriver` module.

Since Selenium 4, `Service` objects are used to handle starting and stoping of the drivers. We will use them **to initialize webdriver**. You shall change the module name to the browser of choice, if not using Chrome WebDriver (e.g. `from selenium.webdriver.firefox.service import Service`).

Class `By` acts as a set of different locator strategies that we will be using to **locate HTML elements** on the website.

### Initializing the web driver

```python
# Contents of main function
service = Service(executable_path='driver/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.python.org/jobs/')
```

We start with instantiating a new object of `Service` class, which will be next passed as a argument when invoking an WebDriver object, in example from `webdriver.Chrome` class.

* ⚠️ Since Selenium 4, directly invoking WebDriver with `executable_path` argument is **depreciated**.

The `driver` object will be frequently used in all of our examples. It serves, using so called wire protocol, as a middleman between the script and the web browser. Here, a very common method `get` is used to navigate to the website passed as an argument.

* ✅ The capabilities of WebDriver extend way beyond locating the elements or loading web pages. It can **interact with the websites** using keys or simulating the mouse movement, execute JavaScript code, and many more. 

  Some of those functionalities will be discovered closely in next parts of the course!

### Getting the job listings

```python
jobs_list = driver.find_element(
    by=By.CLASS_NAME, 
    value='list-recent-jobs.list-row-container.menu'
)

listings = jobs_list.find_elements(by=By.TAG_NAME, value='li')
```

If you examine the source code of the website we're working with, you will discover (at least as of the day when this walkthrough has been published) that all of the offers (`<li>` tag) are kept as **items of the ordered list** (`<ol>` tag). To get the information of desire from job listings, we shall address each of those listings individually.

In Selenium, one of the most fundamental aspects is obtaining element references to work with. The most commonly used method is using `find_element`, or `find_elements` method *(note the plurality!)*. This function can be called **both on the driver instance, and on the web element**, to evaluate (search though) entire DOM and only child element of the parent, respectively. Among those methods, Selenium offers a wide range of built-in locator strategies to uniquely identify an element, or subset of elements, listed inside previously mentioned `By` class.

* ✅ Even though it might be confusing at the first glance, it is often useful to narrow the scope of the search of some element that can be difficult to uniquely locate.

In the example, we start with retrieving the list HTML element, and locate it using its class name, `list-recent-jobs.list-row-container.menu`, passed as the locator value among the locator strategy to `find_element`, which returns an instance of `WebElement` class - the reference to HTML element present on the website.

After getting the necessary reference (and storing it as `jobs_list` variable), we want to retrieve the items of the list. The `find_elements` method is called on the element object, to narrow the scope of the search, with `By.TAG_NAME` strategy to find list items, which start with `<li> tag.`. In result, a **list of `WebElement` objects** is returned.

* ⚠️ Even though the method `find_element_by_class_name` will return the same results as `find_element(by=By.CLASS_NAME,[...])`, since Selenium 4 it is recommended to use `find_element` only, with appropriate locator strategy (`By`).

### Iterating though web elements
```python
for item in listings:
    position_elem = item.find_element(
        by=By.CLASS_NAME, 
        value='listing-company-name'
    )

    position_name = position_elem.find_element(
        by=By.TAG_NAME, value='a'
    ).text

    print('Position: ', position_name)
```

We're almost there! The previously called `find_elements` method returned list, an iterable, of WebElements. Now, we just need to consider each listing individually and get the desired information.

Probably the most convenient way to assess each object individually is by iterating over the list using `for` loop. Job position name is kept as a inner text of `<a>` tag, among some other stuff inside `<span>` element. The parent can be uniquely located by its class name, `listing-company-name`. Note that the method `find_element` is once again called on `WebElement` (`item` variable), not on the `driver`, since we're only interested in searching over a particular item inside list tag.

The `find_element` method is once again called, to retrieve the reference to `<a>` tag. However, note the **`.text` call** that follows. It is an **property of WebElement object** that is used to **obtain inner text** from inside of the element.

*Voilà!* The string text is stored as `position_name` and printed to the console.

### Closing the driver
```python
driver.quit()
```

The web browser can be now gracefully closed using `driver.quit()` method. You shall quit the instantiated driver object every time upon finishing your job.

* ✅ While it may not prove to be necessary yet, it is a good practice to call this method manually, since not doing so may result in crashing sessions, especially under more advanced conditions, e.g. remote scraping.

### Invoking main function

```python
if __name__ == '__main__':
    main()
```

This is just a pythonic boilerplate code to protect invoking the script unintentionally and separate the main script logic into a function.

# Upon completion

Congratulations! You've learned how to crawl the website and extract the data programmatically with Selenium.

Some **key takeaways** to help you track the progress:
- Module `selenium.webdriver` contains implementations of the individual browser controlling code, like `Chrome` or `Firefox`. Those can be instantiated with an appropriate `Service` object,
- Methods `find_element` or `find_elements` *(the plurality!)* are used to locate web elements on website DOM, or the subset of it, and can be called both on the driver instance, and on another located element,
- Elements are uniquely addressed with locator strategies, that are kept as attributes of `By` Class, inside the `selenium.webdriver.common.by` module,
- Attributes of `WebElement` objects, such as `text`, are used to retrieve information from the website.

Up next, we will discover ways to interact with the website and expand the application. Switch to branch `2-interactions`, or use the link [here](https://github.com/k-kedzierski/dsc-web-scraping/tree/1-first-script).

# Appendix

- 📝 [Webinar slides](https://docs.google.com/presentation/d/1T8sd_gemHFXScLuROvDglLGzZhAWxFsW-ptaP695n0Y/edit?usp=sharing)
- ✅ [Selenium documentation](https://www.selenium.dev/documentation/)
- 🐍 [Python usage guide](https://docs.python.org/3/using/)

# Project status

Created 12-2021 by [Kacper Kędzierski](https://github.com/k-kedzierski).