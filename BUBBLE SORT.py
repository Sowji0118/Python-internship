def selectionsort(lst):
    for i in range(len(lst)):
        min_value=min(lst[i:])
        min_index=lst.index(min_value, i)
        lst[i], lst[min_index]=lst[min_index], lst[i]


lst=[64,25,12,22,11]
print("Unsorted list:",lst)

selectionsort(lst)
print("sorted list:",lst)
