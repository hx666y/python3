
def count_words(text,words):
    result = 0
    for w in words:
        if w in text.lower():
            result += 1
    return result


if __name__ == '__main__':

    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1