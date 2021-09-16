class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        searched_index = 2
        count = 0
        if ruleKey == "type":
            searched_index = 0
        elif ruleKey == "color":
            searched_index = 1
        for i in range(len(items)):
            if items[i][searched_index] == ruleValue:
                count += 1
        return count