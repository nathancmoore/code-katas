"""Take a string, remove the WUBS, and give it back meaningfully.

#1 Best Practices Solution by isbadawi et al.

def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

"""


def song_decoder(song):
    """Take a string, remove the WUBS, and give it back meaningfully."""
    wubs_removed = song.split("WUB")
    without_blanks = []
    for word in wubs_removed:
        if word != '':
            without_blanks.append(word)
    return ' '.join(without_blanks)
