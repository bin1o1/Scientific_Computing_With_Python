'''This program utilizes merge sort algorithm to sort data. It goes as follows:
We split the array into two halves (divide). Then we recursively apply merge sort 
on both halves until each subarray has only one element(conquer). After that, we 
merge the sorted halves back together to produce a sorted array (merge).'''


def merge_sort(array):      
    if len(array) <= 1:
        return
    #calculating the middle point of array and then creating two subarrays (left and right) with half the elements on each subarray
    middle_point = len(array) // 2      
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    #first recursive call
    merge_sort(left_part)       #executes till the left_part sub array is divided into individual elements 
    merge_sort(right_part)      #

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))