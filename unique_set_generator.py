import random

def generate_unique_sets(start, end, num_per_set):
    """Generates multiple sets of unique random numbers within a given range.

    Args:
        start: The lower bound of the range.
        end: The upper bound of the range.
        num_per_set: The number of numbers in each set.

    Returns:
        A list of sets containing unique random numbers.
    """

    all_numbers = list(range(start, end + 1))
    num_sets = len(all_numbers) // num_per_set  # Calculate number of full sets

    unique_sets = []
    for _ in range(num_sets):
        unique_set = random.sample(all_numbers, num_per_set)
        unique_sets.append(unique_set)
        all_numbers = [num for num in all_numbers if num not in unique_set]  # Remove used numbers

    # Handle any remaining numbers
    if all_numbers:
        unique_sets.append(all_numbers)  # Add remaining numbers as a final set

    return unique_sets

# Get user input
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
num_per_set = int(input("How many numbers do you want in each set? "))

# Generate the unique sets
unique_sets = generate_unique_sets(start, end, num_per_set)

# Print the generated sets
for i, set_ in enumerate(unique_sets):
    print(f"Set {i + 1}: {set_}")
