# VK Console App
Консольное приложение для работы с VK API.

## Как использовать
1. Убедитесь, что у вас установлен Python 3.7+.
2. Клонируйте репозиторий: git clone https://github.com/LizzBizzLol/vk_app.git cd vk_app
3. Установите зависимости (если нужны).
4. Запустите приложение: python main.py --user-id <YOUR_USER_ID> --output-path output.json

Если `--user-id` не указан, будет использован текущий пользователь.
Если `--output-path` не указан, результат сохранится в `output.json`.

## Результат
JSON-файл с информацией о пользователе, подписчиках и подписках.
