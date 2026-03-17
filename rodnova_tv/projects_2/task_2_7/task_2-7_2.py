sequences =\
    ["ATATACGGCGTA",
    "CTTCGGNGGGA"]

for seq in sequences:
    print("Последовательность целиком:")
    print(seq)
    print()

    print("Та же последовательность, но по одному символу:")
    for nucleotide in seq:
        print(nucleotide)

    print("-" * 20)

print("Цикл выполнен")