import random

def random_gold(ran):
    gold = 0
    if ran == 'farm':
        gold += random.randrange(10, 20)
    if ran == 'cave':
        gold += random.randrange(5, 10)
    if ran == 'house':
        gold += random.randrange(2,5)
    if ran == 'casino':
        gold += random.randrange(-50, 50)
    print gold

ran = raw_input()
random_gold(ran)
