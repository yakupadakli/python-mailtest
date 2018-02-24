from mailtest.client import Client


class Api(Client):
    """MailTest API"""
    BASE_URL = "https://api.mailtest.in"
    VERSION = "/v1"

    def __init__(self, **kwargs):
        super(Api, self).__init__(self, **kwargs)
        self.version = self.VERSION
        self.base_url = "%s%s" % (self.BASE_URL, self.version)

    def check(self, domain):
        return self._get(domain)
