
class Action(object):
    def __init__(self, name:str, direction:str = ''):
        self.name = name
        self.direction = direction

    def __repr__(self,) ->str :
        return str(self.name)

table_of_actions = {
        'N': Action('move', 'N'),
        'S': Action('move', 'S'),
        'L': Action('move', 'L'),
        'O': Action('move', 'O'),
        'P': Action('pickup'),
        'X': Action('shoot', 'L'),
        'Y': Action('shoot', 'O'),
        'Z': Action('shoot', 'N'),
        'C': Action('shoot', 'S')
    }