import collections
import re


# def mostCommonWord(self, paragragh: str, banned: List[str]) -> str:
paragragh = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
words = [word for word in re.sub(r'[^\w]', ' ', paragragh).lower().split() if word not in banned]
print(words)
counts = collections.Counter(words)
print(counts.most_common(1)[0][0])
    # return counts.most_common(1)[0][0]

