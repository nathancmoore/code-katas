"""Compare a list of strings to a string and returns the most similar.

#1 Best Practices Solution by kjmosher:

def answer(question, information):
    score, info = max((sum(word in info.lower().split() for word in question.lower().split()), info) for info in information)
    return None if not score else info

"""


def answer(question, information):
    """Compare a list of strings to a string and return the most similar."""
    question_word_list = question.split()
    information_word_list = []
    matches = []

    for str in information:
        information_word_list.append(str.split())

    for answer_words in information_word_list:
        similarity = 0
        for answer_word in answer_words:
            for question_word in question_word_list:
                if answer_word.lower() == question_word.lower():
                    similarity += 1

        matches.append(similarity)
    if max(matches) != 0:
        return information[matches.index(max(matches))]
    return None
