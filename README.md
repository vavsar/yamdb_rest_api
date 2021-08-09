# REST API для сервиса - база отзывов о фильмах, книгах и музыке.

С использованием Continuous Integration и Continuous Deployment.
При пуше в ветку main автоматически отрабатывают сценарии:
1. Автоматический запуск тестов,
2. Обновление образов на Docker Hub,
3. Автоматический деплой на боевой сервер,
4. Отправка сообщения в телеграмм-бот в случае успеха.

## Начало работы

1. Клонируйте репозиторий на локальную машину.
```
git clone <адрес репозитория>
```
2. Для работы с проектом локально - установите вирутальное окружение и восстановите зависимости.
```
python -m venv venv
pip install -r requirements.txt 
```

### Подготовка удаленного сервера для развертывания приложения

Для работы с проектом на удаленном сервере должен быть установлен Docker и docker-compose.
Эта команда скачает скрипт для установки докера:
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
Эта команда запустит его:
```
sh get-docker.sh
```
Установка docker-compose:
```
apt install docker-compose
```
Создайте папку проекта на удаленном сервере и скопируйте туда файлы docker-compose.yaml, Dockerfile, host.conf:
```
scp ./<FILENAME> <USER>@<HOST>:/home/<USER>/yamdb_final/
```

### Подготовка репозитория на GitHub

Для использования Continuous Integration и Continuous Deployment необходимо в репозитории на GitHub прописать Secrets - переменные доступа к вашим сервисам.
Переменые прописаны в workflows/yamdb_workflow.yaml

* DOCKER_PASSWORD, DOCKER_USERNAME - для загрузки и скачивания образа с DockerHub 
* USER, HOST, PASSPHRASE, SSH_KEY - для подключения к удаленному серверу 
* TELEGRAM_TO, TELEGRAM_TOKEN - для отправки сообщений в Telegram

### Развертывание приложения

1. При пуше в ветку main приложение пройдет тесты, обновит образ на DockerHub и сделает деплой на сервер. Дальше необходимо подлкючиться к серверу.
```
ssh <USER>@<HOST>
```
2. Перейдите в запущенный контейнер приложения командой:
```
docker container exec -it <CONTAINER ID> bash
```
3. Внутри контейнера необходимо выполнить миграции и собрать статику приложения:
```
python manage.py collectstatic --no-input
python manage.py migrate
```
4. Для использования панели администратора по адресу http://0.0.0.0/admin/ необходимо создать суперпользователя.
```
python manage.py createsuperuser.
```
5. К проекту по адресу http://0.0.0.0/redoc/ подключена документация API. В ней описаны шаблоны запросов к API и ответы. Для каждого запроса указаны уровни прав доступа - пользовательские роли, которым разрешён запрос.

## Технологии используемые в проекте
Python, Django, Django REST Framework, PostgreSQL, Nginx, Docker, GitHub Actions

![yamdb_workflow](https://github.com/vavsar/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
