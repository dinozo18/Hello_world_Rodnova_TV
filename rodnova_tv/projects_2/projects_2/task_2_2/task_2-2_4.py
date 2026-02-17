reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (шт.): "))

report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."

print(report)

with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Данные сохранены в файл inventory.txt")