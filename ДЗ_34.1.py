#1.Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и возвращает их в виде списка.
#Пример использования:
#text = "Contact us at info@example.com or support@example.com for assistance."
#emails = extract_emails(text)
#print(emails)  # Вывод: ['info@example.com', 'support@example.com']
from re import findall


def extract_emails(text):
    emails = findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return emails


s = ('You can email me at any time at elnur.ahadov1984@gmail.com. '
     'Also for quick communication I leave my second e-mail address elnur@reseptron.com.')

for email in extract_emails(s):
    print(email)