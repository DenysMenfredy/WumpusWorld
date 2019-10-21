
from action import Action
from random import randint

def agentFunction(state:dict) -> None:
    size = state['tamanho']
    x,y = state['coordenada']
    perceptions = state['perceptions']

    # first column
    if y == 0:
        # first line
        if x == 0:
            if 'shine' in perceptions: return Action('pickup')
            #if ('breeze' in perceptions) and ('stench' in perceptions) and ('shine' in perceptions):
            #    pass
            #elif ('breeze' in perceptions) and ('shine' in perceptions):
            #    pass
            elif ('breeze' in perceptions) and ('stench' in perceptions):
                pass
            elif ('stench' in perceptions) and ('shine' in perceptions):
                pass
            elif ('breeze' in perceptions):
                pass
            elif ('stench' in perceptions):
                pass
        # last line
        elif y == size-1:
            pass
        # midle lines
        else:
            pass
    # last column
    elif y == size-1:
        # first line
        if x == 0:
            if 'shine' in perceptions: return Action('pickup')
            #if ('breeze' in perceptions) and ('stench' in perceptions) and ('shine' in perceptions):
            #    pass
            #elif ('breeze' in perceptions) and ('shine' in perceptions):
            #    pass
            elif ('breeze' in perceptions) and ('stench' in perceptions):
                pass
            elif ('stench' in perceptions) and ('shine' in perceptions):
                pass
            elif ('breeze' in perceptions):
                pass
            elif ('stench' in perceptions):
                pass
        # last line
        elif y == size-1:
            pass
        # midle lines
        else:
            pass

    # midle columns
    else:
        # first line
        if x == 0:
            if 'shine' in perceptions: return Action('pickup')
            #if ('breeze' in perceptions) and ('stench' in perceptions) and ('shine' in perceptions):
            #    pass
            #elif ('breeze' in perceptions) and ('shine' in perceptions):
            #    pass
            elif ('breeze' in perceptions) and ('stench' in perceptions):
                pass
            elif ('stench' in perceptions) and ('shine' in perceptions):
                pass
            elif ('breeze' in perceptions):
                pass
            elif ('stench' in perceptions):
                pass
        # last line
        elif y == size-1:
            pass
        # midle lines
        else:
            pass