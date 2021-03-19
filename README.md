# Bots

> *Цель проекта: Создание различных ботов для разных платформ с целью знакомства с работой API, SQL и Python (ver. 3).*

Файл `config.py` который необходим для работы программ содержит мои личные API ключи, здесь он отсутствует.

Для работы Вам необходимо создать свой файл, например:
```
tokens = {
  'TOKEN_TG': 'YOUR TOKEN',
  'TOKEN_GI': 'YOUR TOKEN'
}
```

## *RandGif*

Запуск приложения осуществляется коммандой:
```sh
% Python3 RandGif.py
```

Бот обрабатывающий каждое сообщение в чате (групповом чате) и по ключевому слову (tag) присылает рандомный `.gif` файл из базы данных [Giphy](https://giphy.com/).

Ключ для поиска слова в тексте это символ - '₽', он редкий и был выбран для теста (Быстро находится на клавиатуре iOS в отличии от '$')

Необходимые библиотеки для работы:
| Library | URL |
| --------| ----------- |
| python-telegram-bot | [GitHub URL](https://github.com/python-telegram-bot/python-telegram-bot) |
| requests | [Requests: HTTP for Humans](https://requests.readthedocs.io/en/master/)|
