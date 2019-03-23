from heuristic_util import register_heuristic

@register_heuristic(name='number of reflexive pronouns')
def count_reflexive_pronoun(sentence):
    reflexive_pronouns = [
        'myself','yourself','yourselves',
        'himself','herself','ourself','ourselves',
        'itself','themselves','themself'
    ]
    count = 0
    for word in sentence:
        if(word in reflexive_pronouns):
            count += 1
    return count

@register_heuristic(name='word count')
def count_words(sentence):
    return len(sentence)

def contains_at_least_one(word_list,topic):
    @register_heuristic(name = 'contains topic word: {0}'.format(topic))
    def contains_topic(sentence):
        for word in sentence:
            if(word in word_list):
                return True
        else:
            return False
    return contains_topic