#!/bin/bash
FILE="students.txt"
echo "1. СУММА ВСЕХ ОЦЕНОК:"
sum=$(awk '{sum+=$2} END {print sum}' "$FILE")
echo "   Сумма оценок: $sum"
echo " 2. СРЕДНЯЯ ОЦЕНКА:"
avg_grade=$(awk '{sum+=$2} END {printf "%.2f", sum/NR}' "$FILE")
echo "   Средний балл: $avg_grade"
echo "3. МАКСИМАЛЬНАЯ ОЦЕНКА:"
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' "$FILE")
echo "   Максимальная оценка: $max"

