from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            length = len(s)
            encoded += f"{length}#{s}"

        return encoded

    def decode(self, encoded: str) -> List[str]:
        decoded= []

        i=0
        while i<len(encoded):
            j=i
            while encoded[j] != "#":
                j+=1

            length = int(encoded[i:j])
            decoded.append(encoded[j+1 : j+1+length])
            i = j+1+length

        return decoded