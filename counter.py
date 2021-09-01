import math

# Kysymyksen oikeat vastaukset tähän
oikeat_vastaukset = [26,13,24,15,16,12,8,3,18,2,1,28,5,20,9,11,35,36,4,23,6,31,27,29,14,30,22,7,25,10,21,33,17,19,32,34,]




# Alla olevaan listaan pelaajat ja heidän vastaukset, muista, että rivit täytyy
# erottaa toisistaan pilkulla (viimeisellä saa olla pilkku, vaikka ei tarvitse,
# tekee copy-pastesta helpompaa kun kaikilla riveillä on pilkku)
pelaajien_vastaukset = [
    ["Pelaaja 1", [36, 28, 12, 7, 2, 25, 4, 13, 1, 18]],
    ["Pelaaja 2", [26, 36, 27, 7, 2, 25, 4, 13, 1, 18]],
    ["Pelaaja 3",   [26, 12, 13, 36, 2, 4, 24, 1, 16, 28]],

]


# Alla koodi, siitä ei tarvitse end-userin välittää

def laske_pelaajien_pisteet():
    for indeksi, pelaajan_vastaus in enumerate(pelaajien_vastaukset):
        pisteet = laske_pelaajan_pisteet(oikeat_vastaukset, pelaajan_vastaus[0], pelaajan_vastaus[1])
        pelaajien_vastaukset[indeksi].append(pisteet)


# countScore on niin sanottu funktio, joka ottaa 3 syötettä: oikeat_vastaukset,
# pelaajan_vastaukset, pelaajan_nimi
def laske_pelaajan_pisteet(oikeat_vastaukset, pelaajan_nimi, pelaajan_vastaukset):
    score_per_correct = len(oikeat_vastaukset) - 1
    pisteiden_summa = 0
    for vastaus_alkio in pelaajan_vastaukset:
        index_ans = pelaajan_vastaukset.index(vastaus_alkio)
        index_gt = oikeat_vastaukset.index(vastaus_alkio)
        score = score_per_correct - abs(index_gt - index_ans)
        pisteiden_summa += score
    return pisteiden_summa

def hae_pelaajan_pisteet(pelaaja):
    return pelaaja[2]

def tulosta_tulokset():
    print("Pelaajien pisteet")
    for index, player in enumerate(pelaajien_vastaukset, start=1):
        print(f"{index}. {player[0]}: {player[2]} pistettä")

laske_pelaajien_pisteet()
pelaajien_vastaukset.sort(reverse=True, key=hae_pelaajan_pisteet)
tulosta_tulokset()
