class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        # print(people)
        for p in people:
            # print(res, p[1], p)
            res.insert(p[1], p)
            
            
        # print(res)
        return res