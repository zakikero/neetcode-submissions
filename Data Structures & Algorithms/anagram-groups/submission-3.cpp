class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> res = {};

        std::unordered_map<std::string, std::vector<std::string>> map = {};

        for (std::string& str : strs) {
            std::vector<int> letters(26, 0);
            for (char& c : str)
                letters[c - 'a']++;

            std::string hash = "";
            for (size_t i = 0; i < letters.size(); i++) {
                hash += "#";
                hash += std::to_string(i);
                hash += std::to_string(letters[i]);
            }

            map[hash].push_back(str);
        }

        for (const auto& [key, value] : map) {
            res.push_back(value);
        }

        return res;
    }
};