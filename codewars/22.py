def same_structure_as(original,other):
    orig, oth = [], []
    for i in range(original):
        if type(i) == list:
            orig.append(len(i))
            # print(i)
            same_structure_as(original[i],other[i])
        else:
            orig.append(1)
    for i in other:
        if type(i) == list:
            oth.append(len(i))
            # print(i)
            same_structure_as(original[i], other[i])
        else:
            oth.append(1)
        print(oth, orig)
    return oth == orig


# print(same_structure_as([1,'[',']'],['[',']',1]))
# print(same_structure_as([1,[1,1]],[2,[2,2]]))
print(same_structure_as([[[],[]]],[[1,1]]))