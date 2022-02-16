

arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]


def find_duplicate_in_array(arr):
    ''' function to find duplicates in array'''
    if type(arr) == list:
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if(arr[i] == arr[j]):
                    print(arr[j])
    else:
        print('please provide the input in a list/array')







if __name__ == '__main__':
    find_duplicate_in_array(arr)
