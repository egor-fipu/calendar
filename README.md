# calendar

## Приложение – календарь бронирования
### Описание: 
- Приложение открывается в браузере в виде календаря на текущий месяц
- Пользователь приложения имеет возможность добавить новую запись на 
произвольную дату в календарь
- Запись имеет следующие поля: 
  - Заголовок, 
  - Описание, 
  - Дата события, 
  - Время начала события, 
  - Время окончания события, 
  - Ответственный за событие
- После внесения всей информации, запись сохраняется в БД и отображается в 
интерфейсе календаря
- События на одно и то же дату и время не допускается. Приложение об этом 
сообщает в ходе добавления
- При клике на событие открывается окно с подробной информацией о нем

### Запуск проекта в dev-режиме

- Установить и активировать виртуальное окружение
- Установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip

pip install -r requirements.txt
``` 

- Выполнить миграции:

```
python manage.py migrate
```

- Запустить проект:

```
python manage.py runserver
```