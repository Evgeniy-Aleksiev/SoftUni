class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [None] * len(s)
        for char, idx in zip(s, indices):
            shuffled[idx] = char

        return "".join(shuffled)