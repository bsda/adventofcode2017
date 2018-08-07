
def is_valid(passphrase):
    if len(passphrase) == len(set(passphrase)):
        return True

def is_not_anagram(passphrase):
    for w in passphrase:
        for w2 in passphrase:
            if w == w2:
                continue
            if sorted(w) == sorted(w2):
                return False
    return True




valid = 0
not_anagram = 0
with open('4.txt', 'r') as f:
    for l in f.readlines():
        passphrase = l.rstrip().split(' ')
        if is_valid(passphrase):
            # valid += 1
            if is_not_anagram(passphrase):
                # not_anagram += 1
                print(f'Valid: {passphrase}')
                valid += 1



print(valid)
print(not_anagram)
