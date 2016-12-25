class Result(object):
    def __init__(self, message=None, code=None, links=None):
        self.message = (message or "").strip()
        self.code = (code or "").strip()
        self.links = links or {}

    @property
    def json(self):
        return {
            "speech": self.message,
            "displayText": self.message,
            "data": {
                "code": self.code,
                "links": self.links,
            },
        }
