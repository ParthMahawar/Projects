inp = raw_input('Enter File Name ')
FileUsed = open(inp)

TempWords = []
Words = []
Sentences = []
WordScores = {}
SentenceScores = {}
inverse = {}

bestsentence = None
sentence2 = None
sentence3 = None
sentence4 = None
sentence5 = None

for line in FileUsed:
    Sentences.append(line.rstrip())
    TempWords.append(line.rstrip().split())

for sublist in TempWords:
    for word in sublist:
        Words.append(word)

for word in Words:
    WordScores[word] = WordScores.get(word,0) + 1

for sentence in Sentences:
    temp = sentence.split()
    SentenceScore = 0
    for word in temp:
        SentenceScore += WordScores[word]
    SentenceScores[sentence] = SentenceScore

for sentence,score in SentenceScores.iteritems():
    if score > bestsentence:
        sentence5 = sentence4
        sentence4 = sentence3
        sentence3 = sentence2
        sentence2 = bestsentence
        bestsentence = score

    elif score > sentence2:
        sentence5 = sentence4
        sentence4 = sentence3
        sentence3 = sentence2
        sentence2 = score

    elif score > sentence3:
        sentence5 = sentence4
        sentence4 = sentence3
        sentence3 = score

    elif score > sentence4:
        sentence5 = sentence4
        sentence4 = score

    elif score > sentence5:
        sentence5 = score

for key in SentenceScores:
    inverse[SentenceScores[key]] = key

Variable = [inverse[bestsentence], inverse[sentence2], inverse[sentence3], inverse[sentence4], inverse[sentence5]]

for sentence in Sentences:
    for thing in Variable:
        if sentence == thing:
            print thing
