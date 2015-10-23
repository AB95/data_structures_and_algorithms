def bubble_sort(list_to_be_sorted):
    # Cast as list so that original is not altered
    sorted_list = list(list_to_be_sorted)
    exchanges = False
    for _ in sorted_list:
        for index in xrange(1, len(sorted_list)):
            if sorted_list[index] < sorted_list[index - 1]:
                sorted_list[index], sorted_list[index - 1] = sorted_list[index - 1], sorted_list[index]
                exchanges = True
        if not exchanges:
            return sorted_list
    return sorted_list

