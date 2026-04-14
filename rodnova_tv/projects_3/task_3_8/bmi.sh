#!/bin/bash
read -p "Введите ваш вес(в кг): " USER_WEiGHT 
read -p "Введите ваш рост(в м): " USER_HIGHT
BMI=$(((USER_WEIGHT/USER_HIGHT^2)*10))
echo "Итоговое значение ИМТ: $BMI"
