# task 1
print("\ntask N1\n")

student = {
    "name": "Mariam Abzianidze",
    "age": 24,
    "courses": ["Python", "Computer Science"]
}

print("Name:", student["name"])
print("Age:", student["age"])

student["Age"] = 25 
student["GPA"] = 4.0

student["address"] = {
    "city": "Khoni",
    "zip_code": "5900"
}

print("Name:", student["name"])
print("Age:", student["Age"])
print("GPA:", student["GPA"])

print(student)

# task 2
print("\ntask N2\n")

print("Keys:", student.keys())
print("Values:", student.values())

for key, value in student.items():
    print(f"{key}: {value}")

if "GPA" in student:
    print("\n'GPA' is in the student dictionary.")
else:
    print("\n'GPA' is not in the student dictionary.")

# task 3
print("\ntask N3\n")

students = [
    {"name": "George", "age": 21, "courses": ["Math", "Physics"]},
    {"name": "Davit", "age": 19, "courses": ["Computer Science", "Math"]},
    {"name": "Mariam", "age": 25, "courses": ["Biology", "Chemistry"]}
]

# Math students
math_students = []
for student in students:
    if "Math" in student["courses"]:
        math_students.append(student["name"])

print("Students taking Math:", math_students)

# age above 20
above_20 = 0
for student in students:
    if student["age"] > 20:
        above_20 += 1

print("Number of students above age 20:", above_20)

# task 4
print("\ntask N4\n")

products = [
    {"name": "Carrot", "price": 2, "quantity": 5},
    {"name": "Mushroom", "price": 8, "quantity": 20},
    {"name": "Broccoli", "price": 6, "quantity": 15},
    {"name": "Tomato", "price": 4, "quantity": 10},
    {"name": "Potato", "price": 1, "quantity": 40}
]

# inventory value
total_inventory_value = 0 
for product in products:
    total_inventory_value += product["price"] * product["quantity"]

print("Total Inventory Value:", total_inventory_value)

# average price
total_price = 0
for product in products:
    total_price += product["price"]

average_price = 0
for product in products:
    average_price = total_price / len(products)

print("Average Price of Products:", average_price)

# Expensive Products 
expensive_products = []
for product in products:
    if product["price"] > 2:
        expensive_products.append(product["name"])  

print("Expensive Products:", expensive_products)

# most expensive product
most_expensive_product = products[0]
for product in products:
    if product["price"] > most_expensive_product["price"]:
        most_expensive_product = product

print("Most Expensive Product:", most_expensive_product["name"]) 

# task 5
print("\ntask N5\n")
