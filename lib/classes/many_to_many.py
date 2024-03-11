class Game:
    def __init__(self, title):
        self._title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 1 <= len(title) <= 15:
            self._title = title
        else:
            raise ValueError   