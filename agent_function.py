
from action import Action
from random import choice

def agentFunction(state:dict) -> None:
    size:int                = state['size']
    x, y                    = state['coordenates']
    perceptions:list(str)   = state['perceptions']
    arrow:bool              = state['arrow']

    # first column
    if y == 0:
        # first line
        if x == 0:
            if 'shine' in perceptions: return Action('pickup')

            elif ('breeze' in perceptions) and ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction = choice(['N','L']))
                
            elif ('breeze' in perceptions):
                return Action('move', direction = choice(['N','L']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction = choice(['N','L']))
                
        # last line
        elif x == size-1:
            if 'shine' in perceptions: return Action('pickup')

            elif ('breeze' in perceptions) and ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction = choice(['S','L']))
                
            elif ('breeze' in perceptions):
                return Action('move', direction = choice(['S','L']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction = choice(['S','L']))

        # midle lines
        else:
            if 'shine' in perceptions: return Action('pickup')

            elif ('breeze' in perceptions) and ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction = choice(['N','L','S']))
                
            elif ('breeze' in perceptions):
                return Action('move', direction = choice(['N','L','S']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction = choice(['N','L','S']))

    # last column
    elif y == size-1:
        # first line
        if x == 0:
            if 'shine' in perceptions: return Action('pickup')
            elif ('breeze' in perceptions) and ('stench' in perceptions):
                pass
            elif ('breeze' in perceptions):
                pass
            elif ('stench' in perceptions):
                pass
        # last line
        elif x == size-1:
            pass
        # midle lines
        else:
            pass

    # midle columns
    else:
        # first line
        if x == 0:
            if 'shine' in perceptions: return Action('pickup')
            elif ('breeze' in perceptions) and ('stench' in perceptions):
                pass
            elif ('breeze' in perceptions):
                pass
            elif ('stench' in perceptions):
                pass
        # last line
        elif x == size-1:
            pass
        # midle lines
        else:
            pass