# party_planner.py

# Predefined party items and their values
party_items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11),
]

# Displparty items
print("Available Party Items:")
for index, (name, value) in enumerate(party_items):
    print(f"{index}: {name} (Value = {value})")

# Take user input for selected items
user_input = input("Enter the indices of the party items you want (e.g., 0, 1, 2): ")
selected_indices = list(map(int, user_input.split(",")))

# Fetch selected items and their values
selected_items = [party_items[i][0] for i in selected_indices]
selected_values = [party_items[i][1] for i in selected_indices]

# Calculate the Base Party Code using bitwise AND
base_code = selected_values[0]
for value in selected_values[1:]:
    base_code &= value

# Adjust the Base Party Code and determine the message
if base_code == 0:
    base_code += 5
    message = "Epic Party Incoming!"
elif base_code > 5:
    base_code -= 2
    message = "Let's keep it classy!"
else:
    message = "Chill vibes only!"

# Render the result in HTML format
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Party Planner</title>
</head>
<body>
    <h1>Party Planner</h1>
    <h2>Selected Items:</h2>
    <p>{', '.join(selected_items)}</p>
    <h2>Base Party Code:</h2>
    <p>{' & '.join(map(str, selected_values))} = {base_code}</p>
    <h2>Final Party Code:</h2>
    <p>{base_code}</p>
    <h2>Message:</h2>
    <p>{message}</p>
</body>
</html>
"""

# Save the HTML output to a file
with open("party_planner_output.html", "w") as file:
    file.write(html_output)

print("\nParty planning complete!")
print("The results have been saved to 'party_planner_output.html'. Open it in a browser to view.")
