Разворачивание приложения:
1. Сделать копию репозитория  git clone https://github.com/gameot/test_app.git
2. Настроить виртуальное окружение. 
3. Установить зависимости из файла requirements.txt
4. Инициализировать БД python manage.py migrate
5. Запустить тестовый сервер python manage.py runserver

Описание API:
Добавление приложения:
- /api/list/ post-запрос для добавления нового приложения

Список приложений:
- /api/list/ get-запрос - выводит список всех приложений (касяк? так как выводится полная информация о приложениях)

Вывод данных о приложении:
- /api/item/$id/?=key -  get-запрос

Обновить данные в приложения:
 - /api/item/$id/ -  put-запрос
 
 Удалить приложение:
 - /api/item/$id/ -  delete-запрос
 
 Сгенерировать ключ для приложения, возвращает сгенерированный ключ:
 - /api/item/$id/update_key/ -  patch-запрос