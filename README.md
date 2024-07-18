## Описание проекта
В Docker были развернуты контейнеры с PostgreSQL и Datahub, с которыми взаимодействет main.go.

main.go выступает в роли API, который запрашивает данные из базы данных и отправляет их на localhost, чтобы убедиться в успешной передаче данных.

В файлах addAPI.py, delete_dataset.py, script.py и test.py реализованы различные функции, обеспечивающие взаимодействие main.go с Datahub.

# Демонстрация Работоспособности
https://github.com/user-attachments/assets/3c7f75cd-4dc5-4b0c-8484-1657a5f6169f

https://github.com/user-attachments/assets/38f92e71-60b7-4619-b018-0968af6ecdcc

# Демонстрация Работоспособности, альтернативного варианта добавления Lineage
(файл test.py)

https://github.com/user-attachments/assets/77d1462b-09f1-4482-b5e1-1abe5a114e9d
