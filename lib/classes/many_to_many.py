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

    def results(self, new_result=None):
        if new_result is not None and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        if new_player is not None and isinstance(new_player, Player):
            if new_player not in self._players:
                self._players.append(new_player)
        return self._players   