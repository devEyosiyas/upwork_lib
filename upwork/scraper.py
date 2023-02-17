def save_to_json(file, data):
    """ Save data to json file """
    import json
    with open('{0}.json'.format(file), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, default=lambda o: o.__dict__))
    print('{0}.json saved with {1} records'.format(file, len(data)))


class Scraper:
    """ The following methods are for the upwork talent profile scraper """
    base_url = 'https://www.upwork.com'
    profile_url = '{0}/search/profiles/'.format(base_url)

    def get_html(self, url):
        """ Returns the html of the url """
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from user_agent import generate_user_agent

        options = Options()
        options.add_argument(f'user-agent={generate_user_agent(device_type="desktop", os=("mac", "linux", "win"))}')
        options.add_argument("--headless")
        options.add_argument("--window-minimize")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        return driver.page_source

    def scrape_upwork_profile(self, page=0, name=''):
        """
        :param page: page number to scrape
        :param name: name of the profile to scrape
        :return: list of upwork talent profiles
        """
        from bs4 import BeautifulSoup

        p_list = []
        if page == 0 and name != '':
            url = self.profile_url + '?q=' + name
        elif page > 0 and name == '':
            url = self.profile_url + '?page=' + str(page + 1)
        elif page == 0:
            url = self.profile_url
        else:
            url = self.profile_url + '?page=' + str(page + 1) + '&q=' + name

        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        if 'Your IP' in html:
            raise CookieException
        for profile in soup.find_all('div', class_='up-card-section up-card-hover'):
            talent = Talent()
            name = profile.find('div', class_='identity-name')
            if name is not None:
                talent.name = name.text.strip()
            image = profile.find('img')
            if image is not None and image.has_attr('src'):
                talent.image = image['src']
            link = profile.find('div', class_='d-flex justify-space-between align-items-start')
            if link is not None:
                talent.link = '{0}/freelancers/{1}'.format(self.base_url, link.decode_contents().split(
                    'data-qa-freelancer-ciphertext="')[1].split('"')[0])
            title = profile.find('p', class_='my-0 freelancer-title')
            if title is not None:
                talent.title = title.text.strip()
            location = profile.find('span', class_='d-inline-block vertical-align-middle')
            if location is not None:
                talent.location = location.text.strip()
            rate = profile.find('div', class_='grid-col-1 grid-col-sm-1 justify-self-start nowrap')
            if rate is not None:
                talent.rate = rate.text.replace('/hr', '').strip()
            earned = profile.find('div', class_='grid-col-2 grid-col-sm-2 justify-self-start nowrap')
            if earned is not None:
                talent.earned = earned.text.split()[0].strip()
            about = profile.find('div', class_='up-line-clamp-v2 clamped')
            if about is not None:
                talent.about = about.text.strip()
            job_success = profile.find('span', class_='up-job-success-text')
            if job_success is not None:
                talent.job_success = job_success.text.split()[0].strip()
            skills = []
            for skill in profile.find_all('div', class_='up-skill-badge'):
                skills.append(skill.text.strip().replace('\n', ''))
            if len(skills) > 0:
                talent.skills = skills
            rank = profile.find('span', class_='status-text d-flex top-rated-badge-status')
            if rank is not None:
                talent.rank = rank.text.strip()
            p_list.append(talent)
        return p_list

    def bulk_profiles(self, max_pages=10, file_name='upwork_profiles'):
        profiles = []
        for i in range(0, max_pages):
            profiles += self.scrape_upwork_profile(i)
        save_to_json(file_name, profiles)


class Talent:
    """ Upwork Talent Class """

    def __init__(self, name=None, image=None, title=None, skills=None, about=None, location=None, link=None, rate=None,
                 earned=None, job_success=None, rank=None):
        self.name = name
        self.image = image
        self.title = title
        self.skills = skills
        self.about = about
        self.location = location
        self.link = link
        self.rate = rate
        self.earned = earned
        self.job_success = job_success
        self.rank = rank

    def __str__(self):
        """ Return the talent as a string """
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}'.format(self.name, self.image, self.title, self.skills,
                                                                     self.about, self.location, self.link, self.rate,
                                                                     self.earned, self.job_success, self.rank)

    def __repr__(self):
        """ Return the talent as a string """
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}'.format(self.name, self.image, self.title, self.skills,
                                                                     self.about, self.location, self.link, self.rate,
                                                                     self.earned, self.job_success, self.rank)

    def __eq__(self, other):
        """ Overrides the default Equals behavior """
        return self.name == other.name and self.image == other.image and self.title == other.title and self.skills == other.skills and self.about == other.about and self.location == other.location and self.link == other.link and self.rate == other.rate and self.earned == other.earned and self.job_success == other.job_success and self.rank == other.rank

    def __hash__(self):
        """ Override the default hash behavior """
        return hash(self.name) ^ hash(self.image) ^ hash(self.title) ^ hash(self.skills) ^ hash(self.about) ^ hash(
            self.location) ^ hash(self.link) ^ hash(self.rate) ^ hash(self.earned) ^ hash(self.job_success) ^ hash(
            self.rank)

    def _to_number_(self):
        """ Convert the earning to a number """
        return float(self.earned.lower().replace('$', '').replace(',', '').replace('+', '').replace('k', '000'))

    def __to_currency__(self):
        """ Convert to currency """
        return '${0:,.2f}'.format(self._to_number_())


class CookieException(Exception):
    """ Raised when cookie expired/ blocked, try changing the cookie and come back... :) """

    def __init__(self):
        """ Constructor """
        self.message = 'Get a new cookie and try again'

    def __str__(self):
        """ Return the message """
        return self.message
