# Upwork Scraper

Upwork Scraper is a Python library for scraping upwork talent profiles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install upwork scraper.

```bash
pip install upwork
```
## Get Cookie
In order to use this library you need a cookie and user agent, pretty easy to get.
I'll show using Google Chrome.

Navigate to [upwork](https://www.upwork.com/search/profiles) and open developer console.

To open the developer console in Google Chrome, open the Chrome Menu in the upper-right-hand corner of the browser window and select More Tools > Developer Tools.

You can also use Option + ⌘ + J (on macOS), or Shift + CTRL + J (on Windows/Linux).

After that type `document.cookie` and hit `Enter` store it somewhere safe.
Next part is getting your user-agent to do that type `navigator.userAgent` in the console and hit `Enter` you got the user-agent, store that one as well, we need it later on.

## Usage

```python
from upwork import Scraper, Talent

# method one

user_agent = '' # paste the user-agent 
cookie = '' # paste the cookie

# initialize the scraper
scraper = Scraper(user_agent=user_agent, cookie='cookie')

# method two

# paste the cookie into the first line and the user-agent into the second line, save the text file
data = open('data.txt', 'r', encoding='utf-8').readlines()

# initialize the scraper using method two
scraper = Scraper(file=data)

# Scrape the first ten profiles
scraper.scrape_upwork_profile()

# Scrape the second ten profiles
scraper.scrape_upwork_profile(page=1)


# Scrape any profile that matches the name john
scraper.scrape_upwork_profile(name='john')

# Scrape the first ten profiles that contain the name john
scraper.scrape_upwork_profile(page=1, name='john')

# saves the first ten pages (100 profiles) to upwork_profiles.json file
scraper.bulk_profiles()


# saves the first ten pages (100 profiles) to profiles.json file
scraper.bulk_profiles(file_name='profiles')


# saves the first ten pages (200 profiles) to sample.json file
scraper.bulk_profiles(max_pages=20, file_name='sample')

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)