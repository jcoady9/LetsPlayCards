
# Copyright (c) 2015 Joshua Coady

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from solitaire import Solitaire
from model.card import Card

testSolitaire = Solitaire()

#test hasComputerOpponent()
assert testSolitaire.hasComputerOpponent() is False

#test moveFoundation()
cards = []
cards.append(Card(3, "3H", "H"))
cards.append(Card(4, "4H", "H"))
cards.append(Card(2, "2H", "H"))
cards.append(Card(2, "2D", "D"))
cards.append(Card(1, "AH", "H"))
cards.append(Card(10, "JH", "H"))

testSolitaire._Solitaire__waste_pile = [card for card in cards]

assert testSolitaire.moveFoundation(Card(1, "AH", "H"), 0) is False
assert testSolitaire.moveFoundation(Card(1, "AH", "H"), 4) is False  # <- sometimes throws a false-negative, don't know why...

assert testSolitaire.moveFoundation(cards.pop(), 1) is False # JH on empty
testSolitaire._Solitaire__waste_pile.pop()
assert testSolitaire.moveFoundation(cards.pop(), 1) is True  # AH on empty
assert testSolitaire.moveFoundation(cards.pop(), 1) is False # 2D on AH
testSolitaire._Solitaire__waste_pile.pop()
assert testSolitaire.moveFoundation(cards.pop(), 1) is True  # 2H on AH
assert testSolitaire.moveFoundation(cards.pop(), 1) is False # 4H on 2H
testSolitaire._Solitaire__waste_pile.pop()
assert testSolitaire.moveFoundation(cards.pop(), 1) is True  # 3H on 2H

#test canMoveToTableau()
cards = []
cards.append(Card(13, "KD", "D"))
cards.append(Card(11, "JS", "S"))
cards.append(Card(10, "10S", "S"))
cards.append(Card(12, "QD", "D"))
cards.append(Card(12, "QS", "S"))
cards.append(Card(12, "QC", "C"))
cards.append(Card(13, "KC", "C"))
cards.append(Card(12, "QC", "C"))

testSolitaire._Solitaire__tableau_piles[0] = []

assert testSolitaire.canMoveToTableau(cards.pop(), testSolitaire._Solitaire__tableau_piles[0]) is False # QC on empty
assert testSolitaire.canMoveToTableau(cards[-1], testSolitaire._Solitaire__tableau_piles[0]) is True    # KC on empty
testSolitaire._Solitaire__tableau_piles[0].append(cards.pop()) 
assert testSolitaire.canMoveToTableau(cards.pop(), testSolitaire._Solitaire__tableau_piles[0]) is False # QC on KC
assert testSolitaire.canMoveToTableau(cards.pop(), testSolitaire._Solitaire__tableau_piles[0]) is False # QS on KC
assert testSolitaire.canMoveToTableau(cards[-1], testSolitaire._Solitaire__tableau_piles[0]) is True    # QD on KC
testSolitaire._Solitaire__tableau_piles[0].append(cards.pop()) 
assert testSolitaire.canMoveToTableau(cards.pop(), testSolitaire._Solitaire__tableau_piles[0]) is False # 10S on QD
assert testSolitaire.canMoveToTableau(cards[-1], testSolitaire._Solitaire__tableau_piles[0]) is True    # JS on QD
testSolitaire._Solitaire__tableau_piles[0].append(cards.pop()) 
assert testSolitaire.canMoveToTableau(cards.pop(), testSolitaire._Solitaire__tableau_piles[0]) is False # KD on JS
