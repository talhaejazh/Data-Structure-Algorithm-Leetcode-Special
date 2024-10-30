class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup=defaultdict(list)
        for s in strs:
            key="".join(sorted(list(s)))
            # print(key)
            if key in lookup:
                lookup[key].append(s)
            else:
                lookup[key]=[s]
        output=[]
        for key in lookup:
            output.append(lookup[key])
            # print(output)
        return output
                
        
        
        
#         lookup=defaultdict(list)
#         for s in strs:
#             key="".join(sorted(list(s)))
#             if key in lookup:
#                 lookup[key].append(s)
#             else:
#                 lookup[key]=[s]
#         output=[]
#         for key in lookup:
#             output.append(lookup[key])
#             print(lookup[key])
#         return output
    
        # for s in strs:
        #     key="".join(sorted(list(s))) #first list then sort and the join as str [abc,abc,abc]
        #     if key in lookup:
        #         lookup[key].append(s) # something like this [1(eat,eat,eat),2(abc,abc)]
        #     else:
        #         lookup[key]=[s]
        # output=[]
        # for key in lookup:
        #     output.append(lookup[key])
        #     print(lookup[key])
        # return output