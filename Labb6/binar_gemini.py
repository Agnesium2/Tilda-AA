def binary_search(arr, target):
    """
    Söker efter 'target' i den sorterade listan 'arr'.
    Returnerar elementet om det hittas, annars None.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return arr[mid]  # Returnerar elementet istället för index
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return None  # Returnerar None istället för -1


def main():
    # Läs in listan
    indata = input().strip()
    the_list = indata.split()
    
    # Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()