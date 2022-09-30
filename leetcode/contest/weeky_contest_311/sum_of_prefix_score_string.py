def solution(words):
    scores = []
    prefixes = get_prefix(words)
    for i in range(len(prefixes)):
        score = 0
        for j in range(len(words)):
            for k in range(len(prefixes[i])):
                if words[j].startswith(prefixes[i][k]):
                    score += 1
        scores.append(score)
    return scores


def get_prefix(words):
    prefixes = []
    for i in range(len(words)):
        word = words[i]
        prefix = [word[:i + 1] for i in range(len(word))]
        prefixes.append(prefix)
    return prefixes


w = ["abc","ab","bc","b"]
print(solution(w))
