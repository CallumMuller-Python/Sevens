import copy
import random
class Card:
    card_value=-2
    suit=-1

class Player:
    def __init__(self):
        self.cards=[]
        self.card_score=0
        self.playable=[]
        self.player_num=-1


class Suit:
    def __init__(self):
        self.cards=[]

hearts=[Card,Card]
diamonds=[Card,Card]
clubs=[Card,Card]
spades=[Card,Card]

def player_playable(player):
    x=[]
    player.playable.clear()
    for i in range(len(player.cards)):
        if(player.cards[i].card_value==7):
            player.playable.append(player.cards[i])
        for j in range(0,4):
           if(j==0):
               x=hearts
           if(j==1):
               x=diamonds
           if(j==2):
               x=clubs
           if(j==3):
               x=spades
           if(player.cards[i].suit==j):
               for k in range(len(x)):
                   if(player.cards[i].card_value==x[k].card_value-1 or player.cards[i].card_value==x[k].card_value+1):
                       player.playable.append(player.cards[i])

def play(card):
    if(card.card_value==7):
        if(card.suit==1):
            diamonds[0]=card
            diamonds[1]=card
        if (card.suit == 2):
            clubs[0] = card
            clubs[1] = card
        if (card.suit == 3):
            spades[0] = card
            spades[1]=card
        return
    if(card.suit==0):
        if(card.card_value==hearts[0].card_value-1):
            hearts[0]=card
        if(card.card_value==hearts[len(hearts)-1].card_value+1):
            hearts[1]=card
    if (card.suit == 1):
        if (card.card_value == diamonds[0].card_value - 1):
            diamonds[0] = card
        if (card.card_value == diamonds[len(diamonds) - 1].card_value + 1):
            diamonds[1] = card
    if (card.suit == 2):
        if (card.card_value == clubs[0].card_value - 1):
            clubs[0] = card
        if (card.card_value == clubs[len(clubs) - 1].card_value + 1):
            clubs[1] = card
    if (card.suit == 3):
        if (card.card_value == spades[0].card_value - 1):
            spades[0] = card
        if (card.card_value == spades[len(spades) - 1].card_value + 1):
            spades[1] = card
#1 hearts
#2 diamonds
#3 clubs
#4 spades


if __name__ == '__main__':
    cardVec=[]
    players =5
    playerVec=[]
    x=Card()
    y=Player()
    count=0
    cardsPlayed=0
    suitVec=[hearts,diamonds,clubs,spades]
    first=0

    for i in range(52):
        cardVec.append(copy.deepcopy(x))
    for i in range(0,4):
        for j in range(1,14):
            cardVec[count].suit=i
            cardVec[count].card_value = j
            count+=1

    random.shuffle(cardVec)

    for i in range(players):
        p = copy.deepcopy(y)
        playerVec.append(p)

    count=0
    while(len(cardVec)!=0):
        count += 1
        for i in range(players):
            if(len(cardVec)!=0):
                playerVec[i].cards.append(cardVec[len(cardVec)-1])
                cardVec.pop()

    for i in range(players):
        print()
        for j in range(len(playerVec[i].cards)):
          print(playerVec[i].cards[j].suit,playerVec[i].cards[j].card_value)

    for i in range(len(playerVec)):
        playerVec[i].player_num=i+1
        for j in range(len(playerVec[i].cards)):
            playerVec[i].card_score+=pow(abs(playerVec[i].cards[j].card_value-7),1)

    for i in range(players):
        for j in range(len(playerVec[i].cards)):
            if(playerVec[i].cards[j].suit==0):
                if(playerVec[i].cards[j].card_value==7):
                    hearts[0]=playerVec[i].cards[j]
                    hearts[1] = playerVec[i].cards[j]
                    playerVec[i].cards.pop(j)
                    print(playerVec[i].player_num, " played first")
                    playerVec.append(playerVec[i])
                    playerVec.pop(i)
                    break

    played=0
    winner=-1
    while(winner==-1):
        print('hearts')
        print(hearts[0].suit, hearts[0].card_value,hearts[1].suit, hearts[1].card_value)
        print('diamonds')
        print(diamonds[0].suit, diamonds[0].card_value,diamonds[1].suit, diamonds[1].card_value)
        print('clubs')
        print(clubs[0].suit, clubs[0].card_value,clubs[1].suit, clubs[1].card_value)
        print('spades')
        print(spades[0].suit, spades[0].card_value,spades[1].suit, spades[1].card_value)
        print()
        for i in range(len(playerVec)):
            player_playable(playerVec[i])
            random.shuffle(playerVec[i].playable)
            if(len(playerVec[i].cards)==0):
                winner=i
                break
            if(len(playerVec[i].playable)>0):
                print(playerVec[i].player_num , "played: " ,playerVec[i].playable[0].card_value,'of', playerVec[i].playable[0].suit,' ', len(playerVec[i].cards))
                print()
                play(playerVec[i].playable[0])
                playerVec[i].cards.remove(playerVec[i].playable[0])
                cardsPlayed += 1
    for i in range(len(playerVec)):
        print(playerVec[i].player_num,': ',playerVec[i].card_score)
    print(winner+'won')




