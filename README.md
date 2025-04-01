## TaskCase API: Создание Задачи

Этот раздел описывает API для создания новой задачи.

### Запрос

**Метод:** `POST`

**URL:** `/tasks/`

**Заголовки:**
Host: localhost:8000
Content-Type: application/json
Accept: application/json



**Тело запроса (JSON):**

```json
{
  "title": "Задача 2",
  "is_completed": false
}
title: (string, required) Заголовок задачи.
is_completed: (boolean, required) Статус завершенности задачи (true - завершена, false - не завершена).
Ответ
Код статуса: 201 Created

Заголовки:


Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
Тело ответа (JSON):


{
  "id": 2,
  "title": "Задача 2",
  "is_completed": false
}
