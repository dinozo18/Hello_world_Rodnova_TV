#!/bin/bash

read -r -p "Введите экспрессию гена(целое число): " expression
read -r -p "Введите название гена: " name_gen
if [[ "$expression" == "" || "$name_gen" == "" ]]; then
    echo -e "Недостаточно входящих данных"
else
echo "Экспрессия гена $name_gen составляет $expression единиц"
fi
