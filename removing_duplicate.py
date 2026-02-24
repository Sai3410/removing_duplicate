
def remove_duplicates_preserve_order(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


lst = [4, 5, 6, 4, 7, 5, 8, 6]
result = remove_duplicates_preserve_order(lst)
print(result)  