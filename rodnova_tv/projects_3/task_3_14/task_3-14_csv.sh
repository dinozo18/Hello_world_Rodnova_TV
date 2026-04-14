#!/bin/bash
FILE="data.csv"
echo "Названия товаров: "
cut -d',' -f2 "$FILE"
echo "Товары дороже 20: "
awk -F',' '$3 > 20 {print "   " $2 " - " $3 "$"}' "$FILE"
total=$(awk -F',' '{sum+=$3} END {print sum}' "$FILE")
echo "   Общая стоимость: $total$"
