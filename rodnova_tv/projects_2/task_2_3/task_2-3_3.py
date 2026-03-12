researcher_name = "Роднова Т.В."
date = "12.03.2026"
experiment_name = "Клонирование"
conclusion = " В ходе эксперимента выявлены нарушения"
with open('journal.txt', 'w', encoding='utf-8') as file:
    print("+" + "-" * 50 + "+\n")
    print(f"|{'Электронный лабораторный журнал'.center(50)}|\n")
    print("+" + "-" * 50 + "+\n")
    print(f"| ФИО исследователя : {researcher_name.center(29)}|\n")
    print(f"| Дата : {date.center(42)}|\n")
    print(f"| Эксперимент : {experiment_name.center(35)}|\n")
    print("+" + "-" * 50 + "+\n")
    print(f"| Вывод: {conclusion}|\n")
    print("+" + "-" * 50 + "+\n")
print("\nФайл 'journal.txt' успешно создан")