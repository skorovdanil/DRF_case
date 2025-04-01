# TaskCase

Минимальное API для работы с задачами

### 1. Создание задачи

**Запрос:**
```url
POST /tasks/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Accept: application/json

{
    "title": "Задача 2",
    "is_completed": false
}
```
**Ответ:**
```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "title": "Задача 2",
    "is_completed": false
}
```
