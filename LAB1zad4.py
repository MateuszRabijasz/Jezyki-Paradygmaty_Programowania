def zadanie4(items, inventory_size):
    for item in items:
        if item["weight"] > inventory_size:
            raise ValueError(
                f"Przedmiot o wadze {item['weight']} przekracza maksymalną pojemność plecaka ({inventory_size})!")

    items_sorted = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)
    current_weight = 0
    selected_items = []
    total_value = 0

    for item in items_sorted:
        if current_weight + item["weight"] <= inventory_size:
            selected_items.append(item)
            current_weight += item["weight"]
            total_value += item["value"]

    return selected_items, total_value



items = [
    {"weight": 2, "value": 2},
    {"weight": 3, "value": 10},
    {"weight": 3, "value": 7},
]

inventory_size = 5


selected_items, total_value = zadanie4(items, inventory_size)

print(f"Wybrane przedmioty: {selected_items}")
print(f"Łączna wartość: {total_value}")