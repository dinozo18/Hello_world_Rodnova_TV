#!/bin/bash
sed -i.bak "s|/var/lib/mysql/data|/mnt/ssd/mysql|g" settings.php
echo "Замена выполнена. Резервная копия сохранена в settings.php.bak"
