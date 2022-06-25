class Talent:
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
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}'.format(self.name, self.image, self.title, self.skills,
                                                                     self.about, self.location, self.link, self.rate,
                                                                     self.earned, self.job_success, self.rank)

    def __repr__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}'.format(self.name, self.image, self.title, self.skills,
                                                                     self.about, self.location, self.link, self.rate,
                                                                     self.earned, self.job_success, self.rank)

    def __eq__(self, other):
        return self.name == other.name and self.image == other.image and self.title == other.title and self.skills == other.skills and self.about == other.about and self.location == other.location and self.link == other.link and self.rate == other.rate and self.earned == other.earned and self.job_success == other.job_success and self.rank == other.rank

    def __hash__(self):
        return hash(self.name) ^ hash(self.image) ^ hash(self.title) ^ hash(self.skills) ^ hash(self.about) ^ hash(
            self.location) ^ hash(self.link) ^ hash(self.rate) ^ hash(self.earned) ^ hash(self.job_success) ^ hash(
            self.rank)

    def __to_number__(self):
        return float(self.earned.lower().replace('$', '').replace(',', '').replace('+', '').replace('k', '000'))

    def __to_currency__(self):
        return '${0:,.2f}'.format(self.__to_number__())
