import random
li = ['ABCDEFGHIJKLMNOPQRST','abcdeffghijklmnopqrstwxyz','1234567890']
def idx_g():
    token = ""
    for i in range(25):
        index = random.randint(0, 2)
        token = token + random.choice(li[index])
    return token