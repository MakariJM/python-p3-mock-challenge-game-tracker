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

    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        return sum(player_scores) / len(player_scores) if player_scores else 0


class Player:
    def __init__(self, username):
        self._username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self, new_result=None):
        if new_result is not None and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        if new_game is not None and isinstance(new_game, Game):
            if new_game not in self._games_played:
                self._games_played.append(new_game)
        return self._games_played