def largestRectangleArea(heights):
    max_area = 0
    for i, height in enumerate(heights):
        for j in range(i+1):
            width = j + 1
            min_height = min(heights[i-j:i+1])
            area = width * min_height
            max_area = max(max_area, area)

    return max_area

def solution(heights):
    heights = heights + [0]
    n = len(heights)
    stack = []

    max_area = 0
    for i in range(n):

        while stack and heights[stack[-1]] > heights[i]:
            index = stack.pop()
            area = (i - stack[-1] - 1) * heights[index] if stack else i * heights[index]
            max_area = max(max_area, area)

        stack.append(i)

    # while stack:
    #     index = stack.pop()
    #     area = (n - stack[-1] - 1) * heights[index] if stack else n * heights[index]
    #     max_area = max(max_area, area)

    return max_area

#    0 1 2 3 4
h = [1,2,3,4,5]
# print(largestRectangleArea(h))
print(solution(h))