# Проект «API для Yatube»
 
### Описание

Yatube - проект социальной сети. «API для Yatube» расширяет возможности социальной сети. Новый функционал позволяет пользователям публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.

#### Реализованы возможности
1. Получение, создание, обновление, удаление публикаций.
2. Получение, создание, обновление, удаление комментариев к публикациям.
3. Просмотр сообществ и детальной информации о них.
4. Отслеживание подписок на авторов, а так же возможность подписки на интересующего автора поста.
5. Получение, обновление и проверка JWT авторизации.

### Стек:
Python==3.7

Django==2.2.16

pytest==6.2.4

djangorestframework==3.12.4

djangorestframework-simplejwt==4.7.2

Pillow==8.3.1

PyJWT==2.1.0

requests==2.26.0

### Запуск проекта. 

1. Клонировать репозиторий и перейти в него в командной строке. 
```
git clone https://github.com/Yana-K38/API_Yatube.git
```
```
cd API_Yatube
```
2. Установите виртуальное окружение и активируйте его: 
``` 
pip install -m venv venv
``` 
``` 
source venv/Scripts/activate
``` 
3. Установите зависимости из файла requirements.txt 
``` 
   pip install -r requirements.txt 
``` 
4. Выполните миграцию: 
``` 
   python manage.py migrate 
``` 
 5. Запустите проект: 
 ``` 
   python manage.py runserver 
``` 
##### После запуска проекта, документация будет доступна по адресу:
```http://localhost:port/redoc/```

### Примеры запросов и ответов. 

##### _GET-запрос_: Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
```
   GET .../api/v1/posts/ 
```
Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
##### _POST-запрос_: Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
   POST .../api/v1/posts/ 
```
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
``` 
Пример ответа: 
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
##### _GET-запрос_: Получение всех комментариев к публикации.
```
GET .../api/v1/posts/{post_id}/comments/ 
```
Пример ответа: 
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
##### _POST-запрос_: Добавление нового комментария к публикации. Анонимные запросы запрещены.
```
POST .../api/v1/posts/{post_id}/comments/ 
```
Пример ответа: 
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
} 
```
##### _GET-запрос_: Получение информации о сообществе по id.
```
GET .../api/v1/groups/id/ 
```
Пример ответа: 
```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```
##### _GET-запрос_: Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
```
GET .../api/v1/follow/ 
```
Пример ответа: 
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```
##### _POST-запрос_: Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
POST .../api/v1/posts/{post_id}/comments/ 
```
Пример ответа: 
```
{
  "user": "string",
  "following": "string"
}
```
