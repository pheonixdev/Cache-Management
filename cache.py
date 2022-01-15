
# global lists, requests and cache
requests = []
cache = []

# main function with the menu to perform fifo, lfu or quit the program
def main():

    cache.clear()
    requests.clear()
    # To get the pages from the user
    userRequests()
    choice =input("\nPress 1 for First In First Out (FIFO)\nPress 2 for Least Frequently Used (LFU):\nPress Q to quit the program ")
    # Putting a check if the user enters a value other than those sepcified in the menu
    while choice not in ('1', '2','q','Q'):
        choice = input("\nInvalid Input...\nPlease Enter 1 or 2 or Q \n")
    if (choice == "1"):
        print("\nYou have selected " ,choice, "\nImplementing First in First Out (FIFO) algorithm")
        fifo()
    if (choice == "2"):
        print("\nYou have selected " ,choice, "\nImplementing Least Frequently Used (LFU) algorithm")
        lfu()
    if (choice == "q" or choice =='Q'):
        print("\nExiting program...")
        exit(0)

# function to get the pages from the user
def userRequests():

    while True:
        elements=input("Please enter the next page to be added to the list of requests: ") 
        global requests
        if elements.isnumeric():
            # when the value is 0, requests is no more appended and it goes back to the main menu
            if int(elements) == 0:
                return None
            # values except 0 are typecasted to int and stored in requests
            else:
                elements=int(elements)
                requests.append(elements)
        else:
            print("Please enter a valid number ")

# First in First Out function
def fifo():

    global cache
    global requests
    for i in requests:
        if i not in cache:
            # new elements are added to the end of the list
            print("Miss")
            cache.append(i)
        else:
            print("Hit")

        while len(cache) > 8:
            # first element is removed as it has longest time since added
            del cache[0]
            if len(cache) <= 8:
                break     
    print(cache)
    return main()

# Least Frequently Used function
def lfu():

    global cache
    global requests
    # empty dictionary to store the frequency
    freq = {}
    cache = []
    for i in requests:
        if i in freq.keys():
            # If present,frequency increased by 1
            freq[i] += 1
            print("Hit")
        else:
            # If not,frequency set to 1
            freq[i] = 1
            print("Miss")
            cache.append(i)

            while len(cache) > 8:
                # less frequency number is selected to remove & if frequency is same then lowest is removed
                matchCache = {key : freq[key] for key in cache}
                toRemove = min(matchCache,key = lambda k:(matchCache[k],k))
                cache.remove(toRemove)
                if len(cache) <= 8:
                    break
    print(cache)
    return main()

if __name__ == '__main__':
    main()
