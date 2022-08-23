# Python starting project
Унифицированный проект для создания регулярных процедур
1. Общий подход к выкачке данных из БД. Вы просто используете одну функцию, она возвращает df
2. Используйте декоратор ```@message_wrapper("Сообщение")``` для Telegram бота

## Как работать с шаблоном

###Технические вещи
1. Зайдите в папку ```resources\passwords\```, дублируйте файл ```passwords_examle.yml```, называйте его  ```passwords.yml``` и меняйте параметры на собственные. <b>Файл в git загружен не будет.</b> Смотрите в ```.gitignore```
2. Зайдите в папку ```resources\settings\```, дублируйте файл ```settings_examle.yml```, называйте его  ```settings.yml``` и меняйте параметры на собственные. <b>Файл в git загружен не будет.</b> Смотрите в ```.gitignore```

###Что делать дальше
В первую очередь, посмотрите файл ```examples\get_data_from_db.py```. В нем реализован пример 2 pipelines c ошибкой и без ошибки

###Джентельменское соглашение
1. Создаете папку внутри базовой папки с названием своего pipeline
2. sql скрипты выносятся в папку ```resources\sql\ваш_проект\```
