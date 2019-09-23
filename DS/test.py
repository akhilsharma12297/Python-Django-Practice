def largestSegment(radii, numberOfGuests):
    areas = [math.pi * r * r for r in radii]

    def possible(x):
        k = 0
        for a in areas:
            k += a // x
            if k >= numberOfGuests:
                return True
        return False

    l, r = 0, max(areas)
    while l + 1e-5 <= r:
        x = (l + r) / 2
        if possible(x):
            l = x
        else:
            r = x
    return str(round(x, 4))def largestSegment(radii, numberOfGuests):

    areas = [math.pi * r * r for r in radii]
    def possible(x):
        k = 0
        for a in areas:
            k += a // x
            if k >= numberOfGuests:
                return True
        return False

    l, r = 0, max(areas)
    while l + 1e-5 <= r:
        x = (l + r) / 2
        if possible(x):
            l = x
        else:
            r = x
    return str(round(x, 4))


if __name__ == '__main__':


   int(input().strip())

    result = largestSegment(radius, numberOfSegments)

    fptr.write(result + '\n')'\n')'\n')