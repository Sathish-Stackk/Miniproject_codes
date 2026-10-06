items = []

while True:
    item = input("Add item (or type done): ")

    if item.lower() == "done":
        break

    items.append(item)

print("\n--- Shopping List ---")

for i, item in enumerate(items, 1):
    print(f"{i}. {item}")

print("Total items:", len(items))
