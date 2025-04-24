#!/bin/bash
# Скрипт для обновления файла update, коммита и пуша изменений

cd "$(dirname "$0")"

DATE=$(date '+%Y-%m-%d %H:%M:%S')
echo "# Этот файл будет обновляться скриптом" > update
echo "Дата последнего обновления: $DATE" >> update

git add update
git commit -m "update: $DATE"
git push
