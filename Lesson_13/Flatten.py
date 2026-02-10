def flatten(lst: list):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

a = flatten([1, [2, 3], [[4], 5], 6])
for i in a:
    print(i)