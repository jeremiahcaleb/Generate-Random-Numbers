# Unique Number Set Generator

**Description:**

This Python code generates multiple sets of unique random numbers within a user-specified range. It automatically determines the number of sets based on the number of numbers per set desired by the user. Any remaining numbers that don't form a full set are included as a final set.

**Usage:**

1. Save the code as a Python file (e.g., `unique_set_generator.py`).
2. Run the code from the command line:

   ```bash
   python unique_set_generator.py
   ```

3. Follow the prompts to enter the starting and ending numbers of the range, and the number of numbers you want in each set.
4. The code will generate and print the unique sets of numbers.

**Example Output:**

```
Enter the starting number of the range: 1
Enter the ending number of the range: 14
How many numbers do you want in each set? 3
Set 1: [10, 2, 12]
Set 2: [5, 4, 7]
Set 3: [14, 11, 13]
Set 4: [3, 9, 6]
Set 5: [1, 8]  # Final set with remaining numbers
```

**Key Features:**

- Generates unique sets of numbers.
- Automatically determines the number of sets.
- Includes any remaining numbers as a final set.
- User-friendly input prompts.
- Clear output formatting.

**Dependencies:**

- Python 3.x
- `random` module (included in the Python standard library)

**Additional Notes:**

- The code ensures that each set contains unique numbers.
- The number of sets generated is limited by the available numbers in the range and the number of numbers per set.
- For more advanced usage or customization, you can modify the `generate_unique_sets` function within the code.
