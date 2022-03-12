
def trapping_rain_water(heights):
    l = len(heights)
    maxLeft = [0] * l
    maxRight = [0] * l

    # start at 1 because i=0 is always 0
    for i in range(1, l):
        maxLeft[i] = max(heights[0:i])

    # start at l-2 because i=l-1 is always 0
    for j in range(l - 2, -1, -1):
        maxRight[j] = max(heights[j + 1:l])

    trapped = 0
    # start at 1 because i=0 is always 0
    for h in range(1, l):
        rain_at_pos = min(maxLeft[h], maxRight[h]) - heights[h]
        if rain_at_pos > 0:
            trapped += rain_at_pos

    return trapped

def trapping_rain_water_optimal(heights):
    length = len(heights)
    maxLeft = heights[0]
    maxRight = heights[length - 1]
    l = 0
    r = length - 1
    total_rain = 0

    while l < r:
        if maxLeft < maxRight:
            l += 1
            if heights[l] > maxLeft:
                maxLeft = heights[l]
            rain_at_pos = maxLeft - heights[l]
        else:
            r -= 1
            if heights[r] > maxRight:
                maxRight = heights[r]
            rain_at_pos = maxRight - heights[r]

        if rain_at_pos > 0:
            total_rain += rain_at_pos


    print(total_rain)
    return total_rain

#trapping_rain_water_optimal([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])