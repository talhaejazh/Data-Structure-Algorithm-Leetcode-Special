class Solution {
public:
    bool isAnagram(string s, string t) 
    { unordered_map <char,int> smap,tmap;
     if (s.length()!=t.length()){
         return false;
     }
     for (int i=0;i<s.length();i++){
         smap[s[i]]+=1;
         tmap[t[i]]+=1;
     }
     return smap==tmap;
    }
};
//     {
//        unordered_map <char, int> smap,tmap;
//         if (s.length()!= t.length()){
//             return false;
//         }
//         for (int i=0;i<s.length();i++){
//             smap[s[i]]+=1;
//             tmap[t[i]]+=1;
            
//         }
//         return smap==tmap;
//     }
// };