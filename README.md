# Upwork Scraper

Upwork Scraper is a Python library for scraping upwork talent profiles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install upwork scraper.

```bash
pip install upwork
```
## Usage

```python
from upwork import Scraper, Talent

# initialize the scraper
scraper = Scraper()

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

## Note
The `requirements.txt` file should list all Python libraries that this library depends on, and they will be installed using:

```
pip install -r requirements.txt
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

