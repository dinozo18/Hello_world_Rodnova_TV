#!/bin/bash
FILE="students.txt"
echo " 1. Студенты с оценкой ВЫШЕ 80 (>80):"
awk '$2 > 80 {print "   " $1 " - " $2 " баллов"}' "$FILE"
echo " 2. Студенты с оценкой НИЖЕ 70 (<70):"
awk '$2 < 70 {print "   " $1 " - " $2 " баллов"}' "$FILE"
echo " 3. Первая строка файла:"
head -n 1 "$FILE" | awk '{print "   " $0}'

