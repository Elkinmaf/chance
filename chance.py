import random

def coin_flip():
    return random.choice(['heads', 'tails'])

def dice_roll():
    return random.randint(1, 6)


# when importing it in bash, not need to put the extension
# for opening it: "python chance.py"
# for importing it: "import chance"
# for using the functions, specify the imported module befor: "chance.coin_flip() or chance.dice_roll()"