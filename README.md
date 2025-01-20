# Обрезка ссылок с помощью VK

Данный скрипт сокращает введенную ссылку с помощью сервиса VK API и показывает количество переходов по ней.

### Как установить

Для работы скрипта нужен ключ доступа API. Получить его можно создав приложение (https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application) c настройками:

- Тип приложения: Web
- Базовый домен: example.com
- Доверенный Redirect URL:  - https://example.com 

Ключ нужно сохранить в файле формата '.env':
```
VK_TOKEN='ключ'
```
## Пример работы
Код для запуска:
```
python main.py 'ссылка на сайт' 
```
В терминале появится ввод для ссылки, которую хотите сократить:
```
Сокращённая ссылка:  https://vk.cc/cwP3Nm
```
> Если ввести уже сокращённую ссылку выведутся количество переходов по этой ссылке. 



Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
