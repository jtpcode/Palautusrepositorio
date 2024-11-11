class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        def sort_by(player):
            return player.points
        
        players = [p for p in self._players if p.nationality == nationality]

        sorted_players = sorted(players,
                                reverse=True,
                                key=sort_by)
        
        return sorted_players