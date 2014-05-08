from random import sample

WORDS = (
    'admirable',
    'alluring',
    'appealing',
    'attractive',
    'beauteous',
    'charming',
    'classy',
    'cosmetic',
    'cute',
    'dazzling',
    'delightful',
    'divine',
    'elegant',
    'enticing',
    'excellent',
    'exquisite',
    'eyebrows',
    'eyes',
    'eyeslashes',
    'face',
    'fair',
    'fascinating',
    'fine',
    'foxy',
    'good-looking',
    'gorgeous',
    'grand',
    'handsome',
    'hot',
    'lights',
    'lips',
    'lovely',
    'magnificent',
    'marvelous',
    'others',
    'ravishing',
    'sexy',
    'shadows',
    'shapely',
    'sightly',
    'statuesque',
    'stunning',
    'well-formed'
)

def words(count):
    word_list = []
    c = len(word_list)

    if count > c:
        count -= c

        while count > 0:
            c = min(count, len(WORDS))
            count -= c
            word_list += sample(WORDS, c)
    else:
        word_list = word_list[:count]
    return ' '.join(word_list)
