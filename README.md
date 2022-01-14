# dsc-web-scraping

Data Science Club web scraping materials, with brief and easy to follow introductory course and examples.

This repository is divided into **branches**, each covering different set of material with increasing complexity. Though it is recommended to follow the instructions below, feel free to explore them all by yourself!

# Installation

## Prerequisities

Before you start, make sure you have previously installed:

- **Python 3.7+**

  Selenium 4.1.0 supports Python 3.7 or above. If you haven't been working with Python before, follow [this official guide](https://docs.python.org/3/using/) and set up the interpreter.

- **Web browser** of choice. Google Chrome is recommended.

- **WebDriver** for your web browser. You can find list of supported web browsers and download links [here](https://www.selenium.dev/ecosystem/). Remember to check browser version first, and download WebDriver accordingly.

  For the sake of clarity, the WebDriver does not need to be present in your shell `$PATH`. All of the examples will initialize WebDrivers from local path. More will be explained later.

## Python dependencies

All examples will use the same set of dependencies.

Setting up an virtual environment (optional, but recommended):

```sh
# Optionally, set up new environment
python3 -m venv ./.venv
# and activate it
source ./.venv/bin/activate
```

**Installing dependencies:**

```sh 
# Install dependencies
python3 -m pip install -r ./requirements.txt
```

Deactivating the virtual environment:

```sh
# Optionally, deactivate the environment
deactivate
```

*Note: if running Python 3 only, replace `python3` with `python`.*

# Ready?

Jump into the first basic example and switch to branch `1-first-script`, or use the link [here](https://github.com/k-kedzierski/dsc-web-scraping/tree/1-first-script).

# Appendix

- 📝 [Webinar slides](https://docs.google.com/presentation/d/1T8sd_gemHFXScLuROvDglLGzZhAWxFsW-ptaP695n0Y/edit?usp=sharing)
- ✅ [Selenium documentation](https://www.selenium.dev/documentation/)
- 🐍 [Python usage guide](https://docs.python.org/3/using/)

# Project status

Created 12-2021 by [Kacper Kędzierski](https://github.com/k-kedzierski).