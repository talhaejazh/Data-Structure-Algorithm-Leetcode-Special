class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
        
//     }
// };
    public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> uniqueNums;
        
        for (int num : nums) {
            // If the current number is already in the set, it's a duplicate
            if (uniqueNums.count(num) > 0) {
                return true;
            }
            
            // Add the number to the set
            uniqueNums.insert(num);
        }
        
        // No duplicates found
        return false;
    }
};