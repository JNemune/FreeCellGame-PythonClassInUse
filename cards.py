import random    # required for shuffle method of Deck

class Card(object):
    ''' Suit and rank are integers, and index into suit_list and rank_list.
        Value is different from rank: for example face cards are equal in value (all 10)
    '''
    # Use these lists to map the integers of suit and rank to nice words.
    # The 'x' is a place holder so that index-2 maps to '2', etc.
    suit_list = ['x','c','d','h','s']
    rank_list = ['x', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']

    def __init__(self, rank=0, suit=0):
        ''' Rank and suit must be integers. This checks that they are in the correct range.
            Blank card has rank and suit set to 0.
        '''
        self.__suit = 0
        self.__rank = 0
        if type(suit) == int and type(rank) == int:
            # only good indices work
            if suit in range(1,5) and rank in range(1,15):
                self.__suit = suit
                self.__rank = rank

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

    def get_value(self):
        ''' Face cards return 10, the rest return their rank values. Aces are low.
        '''
        # ternary expression:
        return self.__rank if self.__rank < 10 else 10

    def equal_suit(self, other):
        '''Returns True if suits are equal.'''
        return self.__suit == other.__suit

    def equal_rank(self, other):
        '''Returns True if ranks are equal.'''
        return self.__rank == other.__rank

    def equal_value(self, other):
        '''Returns True if values are equal.'''
        return self.get_value() == other.get_value()

    def __str__(self):
        ''' Called by print() so you can print a card, just like any other data structure.
        '''
        # Uses rank to index into rank_list of names; uses suite to index into suit_list of names.
        return "{:s}{:s}".format((self.rank_list)[self.__rank], (self.suit_list)[self.__suit])

    def __repr__(self):
        ''' This method is called if you simply enter a card name in the shell.
            It simply calls, the same method that prints a card.
        '''
        return self.__str__()

class Deck(object):
    ''' Deck of cards, implemented as a list of card objects.
        The last card in the deck (list) is the top of deck.
    '''
    def __init__(self):
        self.__deck=[Card(rank,suit) for suit in range(1,5) for rank in range(1,14)]

    def shuffle(self):
        '''Shuffle the deck using a call to random.'''
        random.shuffle(self.__deck)

    def deal(self):
        '''Return the top card from the deck (only if the deck is not empty).'''
        # ternary expression
        return self.__deck.pop() if len(self.__deck) else None

    def cards_count(self):
        '''Returns the number of cards in the deck.'''
        return len(self.__deck)

    def is_empty(self):
        '''Returns True if the deck is empty.'''
        return len(self.__deck) == 0

    def __str__(self, column_max=10):
        ''' Column-oriented printing of a deck.
        '''
        out=list()
        for index,card in enumerate(self.__deck):
            if index%column_max == 0:  # at final column so print a carriage return
                out.append('\n')
            out.append(str(card).rjust(4), end='')
        out.append('\n\n')
        return ''.join(out)

def __repr__(self):
        ''' Messy print deck, if you enter a deck's name in the shell.
        '''
        return self.__str__()