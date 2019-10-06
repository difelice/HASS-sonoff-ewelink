import random

def gen_nonce():
    return ''.join([str(random.randint(0, 9)) for i in range(15)])