def linear_search(arr, target):
    """
    Performs a linear search on a list.

    Args:
        arr (list): The list to search within.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
my_list = [1, 5, 9, 12, 3, 7]
search_target = 12

index = linear_search(my_list, search_target)

if index != -1:
    print(f"Element {search_target} found at index: {index}")
else:
    print(f"Element {search_target} not found in the list.")

# Example of not found
search_target_not_found = 100
index_not_found = linear_search(my_list, search_target_not_found)

if index_not_found != -1:
    print(f"Element {search_target_not_found} found at index: {index_not_found}")
else:
    print(f"Element {search_target_not_found} not found in the list.")