#!/bin/bash
for i in {1..20}; do
 if [ $((i % 2)) -eq 0 ]; then
continue
fi
echo "Счетчик: $i"
if [ $i -eq 15 ]; then
echo "Число 15 найдено!"
break
fi
done
echo "Рассчет окончен"
