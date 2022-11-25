class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashMap=dedfaultfict()
#         for str in strs:
#             count=[0] 
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())