'''
types of structures in data
unit: word, clause, sentence, paragraph
'''

class Transition:
    '''
    Represents two units, one preceeding the other.
    '''
    def __init__(self,head,tail):
        self.pair = (head,tail)

class Topic:
    '''
    Classification of a unit, independent of context.
    For example, the average meaning of a sentence is a topic.
    '''
    pass

class ActSequence:
    '''
    Classification of sequence of units as context.
    For example, the structure of a five-paragraph essay
    can be represented as an ActSequence.
    '''
    pass
