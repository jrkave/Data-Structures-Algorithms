# Simple Insertion Sort

arr = []
while len(arr) < 5:
    try:
        # Get input
        num = int(input("Enter an integer: "))
        
        # Handle first input
        if len(arr) == 0:
            arr.append(num)
            print(arr)
            continue
        
        # Insert in sorted order
        for i in range(len(arr)):
            if num < arr[i]:
                arr.insert(i, num)
                break
        # Append if num is largest in array
        else:
            arr.append(num)
            
        # Print array
        print(arr)
        
    except ValueError:
        print("Invalid entry. Please try again.")
        