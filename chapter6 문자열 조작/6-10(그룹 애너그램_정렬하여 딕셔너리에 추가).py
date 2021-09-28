import collections


# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagrams = collections.defaultdict(list)
print(anagrams)
for word in strs:
    anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    # return anagrams.values()
print(anagrams.values())
