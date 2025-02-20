[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SE7UNEpI)
## Working with Dictionaries

1. **Create a Dictionary:** Define a dictionary called `student` with keys for `name`, `age`, and `courses`. Assign values of your choice.
2. **Access Values:** Print the `name` and `age` of the student.
3. **Modify Values:** Update the `age` value and add a new key-value pair for `GPA`.
4. **Nested Dictionary:** Add a key `address` with another dictionary as the value, containing keys `city` and `zip_code`.


## Dictionary Operations

1. **Keys and Values:** Print all keys and all values of the `student` dictionary separately.
2. Looping: Write a loop that prints each key and its corresponding value.
3. **Check Membership:** Check if `GPA` is a key in the dictionary and print a message confirming it.


## Combining Lists and Dictionaries

1. **List of Dictionaries:** Create a list called `students` containing 3 dictionaries, each representing a different student with `name`, `age`, and `courses` keys.
2. **Filtering:** Using a loop or list comprehension, create a list of names of students who are taking a specific course (e.g., `"Math"`).
3. **Count Occurrences:** Count how many students are above a certain age (e.g., `age` > 20).


## Working with a List of Dictionaries

1. Create a Product List: Define a list called `products`, where each product is represented as a dictionary with `name`, `price`, and `quantity` keys.
2. Total Inventory Value: Calculate the total inventory value by multiplying `price` by `quantity` for each product and summing the results.
3. Average Price: Calculate the average `price` of all `products` in the list.
4. Filter Expensive Products: Create a new list, `expensive_products`, containing products with a `price` greater than a specified amount (e.g., 20).
5. Most Expensive Product: Find the product with the highest price in the list and print its name and `price`.

## Aggregations with Dictionary Values

1. Sales Dictionary: Create a dictionary called sales where keys are product names and values are lists of integers representing monthly sales figures.

```python
sales = {
    "product_a": [5, 8, 12],
    "product_b": [3, 9, 7],
    "product_c": [10, 15, 8],
}
```
2. Total Sales Per Product: Calculate the total sales for each product and print them in a readable format.
3. Average Sales Per Product: Calculate the average monthly sales for each product and print them.
4. Best-Selling Product: Determine which product had the highest total sales and print its name.
5. Overall Sales Sum: Calculate the sum of all sales across all products and print the result.