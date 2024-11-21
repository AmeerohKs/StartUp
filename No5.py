def find_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None  # If no matching value is found

# Example dictionary:
a = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}

# Example usage:
search_value = "value3"
found_key = find_key_by_value(a, search_value)
if found_key:
    print(f"The key for the value '{search_value}' is '{found_key}'.")
else:
    print(f"No key found for the value '{search_value}'.")
