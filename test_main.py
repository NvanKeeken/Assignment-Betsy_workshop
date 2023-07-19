from main import search

def test_search():
    array_term_silver = ['Silver Moon studs', 'Silver flower bangle', 'Lapis lazuli ring']
    array_term_flower = ['Sunflower studs', 'Silver flower bangle']
    none_existing_term = "sweater"
    assert type(search("silver")) == list
    assert search("silver") == array_term_silver
    assert search("Silver") == array_term_silver
    assert search("silve") == array_term_silver
    assert search("flower") == array_term_flower
    assert search("Flower") == array_term_flower
    assert search("flow") == array_term_flower
    assert search(none_existing_term) == []

