def largestRectangleArea(heights):
    max_area = 0
    for i, height in enumerate(heights):
        for j in range(i+1):
            width = j + 1
            min_height = min(heights[i-j:i+1])
            area = width * min_height
            max_area = max(max_area, area)

    return max_area

h = [2,1,5,6,2,3]
print(largestRectangleArea(h))