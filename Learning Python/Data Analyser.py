# Data Analyser - Favourite Fruits
num_friends=int(input("Enter the number of friends you have: "))

fruit_list = []     # List to store favourite fruits
for i in range(num_friends):
    fruits=input("Enter your favourite fruit: ")
    fruit_list.append(fruits)   # Adds (appends) the favourite fruit of each person into a list.
print("Your friends' favourite fruits are: ", fruit_list)

fruit_count = {}  # Dictionary to store count
for fruit in fruit_list: # Count occurrences of each fruit
    if fruit in fruit_count:
        fruit_count[fruit] += 1 # Increment count if fruit already in dictionary
    else:
        fruit_count[fruit] = 1 # Initialize count if fruit not in dictionary

print("Number of each fruit in the list:")
for fruit, count in fruit_count.items():
    print(f"{fruit}: {count}")

# Find the maximum and minimum count of fruits
max_count = max(fruit_count.values())  # highest number of votes
min_count = min(fruit_count.values())  # lowest number of votes

# Find all fruits with the maximum count
most_liked = [fruit for fruit, count in fruit_count.items() if count == max_count]

# Find all fruits with the minimum count
least_liked = [fruit for fruit, count in fruit_count.items() if count == min_count]

print("Most liked fruit(s):", most_liked)
print("Least liked fruit(s):", least_liked)