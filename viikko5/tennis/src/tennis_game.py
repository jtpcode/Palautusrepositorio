LOVE = 0
FIFTEEN = 15
THIRTY = 30
FORTY = 45
GAME = 55

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_player1_score = LOVE
        self.m_player2_score = LOVE

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_player1_score = self.m_player1_score + FIFTEEN
        else:
            self.m_player2_score = self.m_player2_score + FIFTEEN

    def get_score(self):
        score = ""

        if self.m_player1_score == self.m_player2_score:
            score = self.even_score(self.m_player1_score)
            
        elif self.m_player1_score >= GAME or self.m_player2_score >= GAME:
            point_difference = self.m_player1_score - self. m_player2_score
            score = self.advantage_or_win(point_difference)

        else:
            score = self.middle_game(self.m_player1_score, self.m_player2_score)

        return score

    def even_score(self, player1_score):
        score = ""
        if player1_score == 0:
            score = "Love-All"
        elif player1_score == FIFTEEN:
            score = "Fifteen-All"
        elif player1_score == THIRTY:
            score = "Thirty-All"
        else:
            score = "Deuce"
        
        return score
    
    def advantage_or_win(self, point_difference):
        if point_difference == FIFTEEN:
            score = "Advantage player1"
        elif point_difference == -FIFTEEN:
            score = "Advantage player2"
        elif point_difference > FIFTEEN:
            score = "Win for player1"
        else:
            score = "Win for player2"
        
        return score

    def middle_game(self, player1_score, player2_score):
        str_score = ""

        for i in range(1, 3):
            if i == 1:
                score = player1_score
            else:
                str_score = str_score + "-"
                score = player2_score

            if score == LOVE:
                str_score = str_score + "Love"
            elif score == FIFTEEN:
                str_score = str_score + "Fifteen"
            elif score == THIRTY:
                str_score = str_score + "Thirty"
            elif score == FORTY:
                str_score = str_score + "Forty"
            
        return str_score
    