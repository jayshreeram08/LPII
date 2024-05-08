# #Implement Greedy search algorithm for any of the following application:
# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    print("Enter the size")
    n = int(input())
    arr = []
    
    for i in range(n):
        print("enter {} element".format(i))
        no = int(input())
        arr.append(no)
        
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
