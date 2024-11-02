
def isCircularSentence(sentence: str) -> bool:
    words = sentence.split(' ')
    circle = True

    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0]:
            circle = False
            break

    if words[-1][-1] != words[0][0]:
        circle = False

    return circle

