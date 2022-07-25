# CRUD для Yatube 

API для социальной сети блогеров. 

 

### Задача. 

 Необходимо реализовать API для всех моделей приложения. 

  

 Для аутентификации используется JWT-токены. 

 

 Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке  изменить чужие данные должен возвращаться код ответа 403 Forbidden. 

 

### Примеры запросов и ответов. 

 

Пример GET-запроса: Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

 GET .../api/v1/posts/ 

Пример ответа:

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


Пример POST-запроса: Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

POST .../api/v1/posts/ 

{
  "text": "string",
  "image": "string",
  "group": 0
}
 

Пример ответа: 

{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

Пример GET-запроса: Получение всех комментариев к публикации.

GET .../api/v1/posts/{post_id}/comments/ 

Пример ответа: 

[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]

Пример POST-запроса: Добавление нового комментария к публикации. Анонимные запросы запрещены.

POST .../api/v1/posts/{post_id}/comments/ 

Пример ответа: 

{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
} 

Пример GET-запроса: Получение информации о сообществе по id.

GET .../api/v1/groups/id/ 

 

Пример ответа: 

{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}

Пример GET-запроса: Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.

GET .../api/v1/follow/ 

 
Пример ответа: 

[
  {
    "user": "string",
    "following": "string"
  }
]

Пример POST-запроса: Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.

POST .../api/v1/posts/{post_id}/comments/ 

Пример ответа: 

{
  "user": "string",
  "following": "string"
}

### Запуск проекта. 

 

Клонируйте репозиторий. 

 

Установите виртуальное окружение и активируйте его: 

``` 

    pip install -m venv venv 

``` 

 

``` 

   source venv/Scripts/activate 

``` 

 

Установите зависимости из файла requirements.txt 

 

``` 

   pip install -r requirements.txt 

``` 

Выполните миграцию: 

``` 

   python manage.py migrate 

``` 

 Запустите проект: 

 ``` 

   python manage.py runserver 

``` 

 

### Автор. 

 

Яна Курзюкова 
