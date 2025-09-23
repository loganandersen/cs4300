def word_count() :
    """Opens up task6_read_me.txt and counts the words"""
    with open("task6_read_me.txt") as f :
        # read f, split it into list of words, find length of list
        return len(f.read().split())
