class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # result = [0] * n
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j -i
        #             break
        # return result

        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result 