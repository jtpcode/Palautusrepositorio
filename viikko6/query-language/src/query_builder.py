from matchers import All, PlaysIn, And, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, matcher = []):
        self.matchers = matcher

    def plays_in(self, team):
        self.matchers.append(PlaysIn(team))
        return QueryBuilder(self.matchers)
    
    def has_at_least(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(self.matchers)
    
    def has_fewer_than(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(self.matchers)

    def build(self):
        if not self.matchers:
            return All()
        return And(*self.matchers)
