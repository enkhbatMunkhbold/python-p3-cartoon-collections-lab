def roll_call_dwarves(col):
    for i in range(len(col)):
        print(f"{i + 1}. {col[i]}")

def summon_captain_planet(col):
    return [(call + '!').title() for call in col]

def long_planeteer_calls(col):
    for s in col:
        if len(s) > 4:
            return True
    return False

def find_the_cheese(data):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for s in data:
        if s in cheeses:
            return s
