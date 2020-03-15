def find_anagrams(word, candidates):
    return [c for c in candidates if word.lower() != c.lower() and ''.join(sorted(word.lower())) == ''.join(sorted(c.lower()))]
