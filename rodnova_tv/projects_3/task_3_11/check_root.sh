#!/bin/bash
check_root() {
if [ "$EUID" -ne 0 ]; then
        echo "Ошибка: Этот скрипт должен быть запущен от имени суперпользователя (root)!"
        echo "Пожалуйста, используйте: sudo $0"
        exit 1
    else
        echo "Успех: Скрипт запущен от имени root"
    fi
}
check_root
echo "Текущий пользователь: $(whoami)"
echo "EUID: $EUID"
echo "Скрипт успешно завершил работу"
