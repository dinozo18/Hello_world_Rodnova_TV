name = input("Введите название питательной среды: ")
agar = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")

with open('recipe.txt', 'w', encoding='utf-8') as file:
    file.write(f"=== {name} ===\n")
    file.write(f"\tКонцентрация агара: {agar}%\n")
    file.write(f"\tТемпература стерилизации: {temperature}°C\n")
    
print("\nФайл 'recipe.txt' успешно сформирован!")    