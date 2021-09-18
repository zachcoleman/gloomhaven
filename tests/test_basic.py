import gloomhaven as gh


def test_shuffle():
    deck = gh.GloomhavenDeck()

    deck.shuffle_deck()
    a = deck.current_deck.copy()

    deck.shuffle_deck()
    b = deck.current_deck.copy()

    assert a != b


def test_empty_deck():
    deck = gh.GloomhavenDeck(cards=[])
    deck.shuffle_deck()
    deck.draw_card()


def test_continous_deck():
    deck = gh.GloomhavenDeck(cards=["1"])
    deck.shuffle_deck()
    for _ in range(10):
        assert deck.draw_card() == "1"
