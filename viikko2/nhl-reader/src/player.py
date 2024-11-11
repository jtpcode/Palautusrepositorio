class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
        self.nationality = dict['nationality']
    
    def __str__(self):
        return f"{self.name:20}{self.team:4}{self.goals:3} +{self.assists:3} = {self.points}"
