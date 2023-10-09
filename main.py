import requests
import re


def extract_phone_numbers(text):
    new_phone_numbers = list()
    phone_pattern = re.compile(r'(\+?[78]\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}|\b8\d{10}\b)')
    phone_numbers = re.findall(phone_pattern, text)

    for number in phone_numbers:
        digits_only = re.sub(r'\D', '', number)
        digits_only = re.sub('7', '8', digits_only, 1)
        new_phone_numbers.append(digits_only)
    return list(set(new_phone_numbers))


def find_phone_numbers(url):
    response = requests.get(url)
    response.raise_for_status()
    page_content = response.text

    phone_numbers = extract_phone_numbers(page_content)

    return phone_numbers


if __name__ == "__main__":
    urls = [
        "https://hands.ru/company/about",
        "https://repetitors.info",
    ]

    for url in urls:
        print(f"Поиск номеров на странице: {url}")
        phone_numbers = find_phone_numbers(url)
        if phone_numbers:
            print(f"Найденные номера телефонов:")
            for phone_number in phone_numbers:
                print(phone_number)
        else:
            print("Номера телефонов не найдены.")
