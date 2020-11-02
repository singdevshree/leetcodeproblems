import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ").replace("/", " ").replace(";", " ").replace("'", " ")
        
        
        arr= paragraph.lower().split()        
        
        cntPara= collections.Counter(arr)       
        
        tr= OrderedDict(cntPara.most_common())
        for i in tr.keys():
            if i not in banned:
                return i
            
