# -*- coding: utf-8 -*-

from random import randint
import random

class Card(object):
    def __init__(self, arg_card_suit, arg_card_number):
        self.card_suit =  arg_card_suit
        self.card_number = arg_card_number
        
class Cards(object):
    _list_cards = []
    
    def __init__(self):
        pass
        
    def put_a_card_in_deck(self, arg_new_card):
        self._list_cards.append(arg_new_card)
        
    def get_cards_deck(self):
        return self._list_cards
        
class PilesSet(object):
    dict_piles = {}
    list_discard_cards = []
    
    
if __name__ == "__main__":
    cards_deck = Cards()
    piles_set = PilesSet()
    
    for ith in range(1, 14, 1):
        new_card = Card('diamond', ith)
        cards_deck.put_a_card_in_deck(new_card)
        
    for ith in range(1, 14, 1):
        new_card = Card('heart', ith)
        cards_deck.put_a_card_in_deck(new_card)
        
    for ith in range(1, 14, 1):
        new_card = Card('club', ith)
        cards_deck.put_a_card_in_deck(new_card)
        
    for ith in range(1, 14, 1):
        new_card = Card('spade', ith)
        cards_deck.put_a_card_in_deck(new_card)
    
    
    my_cards_deck = cards_deck.get_cards_deck()
        
    random.shuffle(my_cards_deck)
    while True:
        picked_card = my_cards_deck.pop()
        
        selected_pile_index = (8 * picked_card.card_number / 13)
        
        upward = True
        downward = True
        
        while True:
            if selected_pile_index > 8 or selected_pile_index < 1:
                piles_set.list_discard_cards.append(picked_card.card_number)
                break
            if not piles_set.dict_piles.has_key(selected_pile_index):
                piles_set.dict_piles[selected_pile_index] = picked_card.card_number
                break
            elif piles_set.dict_piles[selected_pile_index] == picked_card.card_number:
                break
            elif piles_set.dict_piles[selected_pile_index] < picked_card.card_number and upward:
                selected_pile_index += 1
                downward = False
            elif piles_set.dict_piles[selected_pile_index] > picked_card.card_number and downward:
                selected_pile_index -= 1
                upward = False
                
            elif upward and piles_set.dict_piles[selected_pile_index] > picked_card.card_number:
                break
            elif downward and piles_set.dict_piles[selected_pile_index] < picked_card.card_number:
                break
                
        if len(piles_set.list_discard_cards) >= 5:
            print "you lose"
            print piles_set.list_discard_cards
            break
        if len(piles_set.dict_piles.keys()) == 8:
            print "you win"
            print piles_set.dict_piles
            break
        if len(my_cards_deck) < 1:
            break
        
        
        
        
        
        
        