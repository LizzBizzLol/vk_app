import requests
import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description="VK Console App")
    parser.add_argument('--user-id', type=str, default=None, help="VK User ID")
    parser.add_argument('--output-path', type=str, default='output.json', help="Path to save the JSON file")
    return parser.parse_args()

def vk_api_request(method, token, params):
    url = f"https://api.vk.com/method/{method}"
    params.update({
        "access_token": token,
        "v": "5.131"
    })
    response = requests.get(url, params=params)
    response.raise_for_status()  # Поднять исключение при ошибке HTTP
    data = response.json()
    if "error" in data:
        raise ValueError(f"Error from VK API: {data['error']['error_msg']}")
    return data["response"]

def main():
    args = parse_arguments()
    token = "vk1.a.l4ZHRDJ53NWEhSkxQdqppvuvBbOly2hZyLlqe6yhnV8jXZs4MZMnYzVDETRoq852wrMy_moaw4Kw01FPU04h2Gc_OiFkFDaS1_VV_WbqWCf57wmDg17SfAbdL3wTnAHUJtnpHZpqzuA-GPrn25Av_eNmn2ZuWqmsWYEbgi0PVTcrnqJKQnrGmzsRc8tKvCVr"  # Вставь токен сюда
    
    user_id = args.user_id if args.user_id else "me"  # Если ID не указан, берем текущего пользователя
    output_path = args.output_path

    try:
        print("Получаем информацию о пользователе...")
        user_info = vk_api_request("users.get", token, {"user_ids": user_id})
        
        print("Получаем подписчиков...")
        followers = vk_api_request("users.getFollowers", token, {"user_id": user_id})
        
        print("Получаем подписки...")
        subscriptions = vk_api_request("users.getSubscriptions", token, {"user_id": user_id})

        result = {
            "user_info": user_info,
            "followers": followers,
            "subscriptions": subscriptions,
        }

        print("Сохраняем результат в JSON...")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        print(f"Данные сохранены в {output_path}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
