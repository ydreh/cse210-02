from random import randint

class Card:
    """A card with a value between 1 and 13

    Attributes:
        value(int): The number value of the card
    """
    def __init__(self):
        """Create a new card
        
        Args:
            self(Card): An instance of card.
        """
        self.value = 0

    def draw(self):
        self.value = randint(1,13)
        