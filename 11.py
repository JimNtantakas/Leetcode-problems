def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        current_height = min(height[left], height[right])
        current_width = right - left
        current_water = current_height * current_width
        max_water = max(max_water, current_water)

        # Move the pointer that points to the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

result=maxArea([1,2,3,4])
print(result)