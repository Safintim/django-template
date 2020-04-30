import requests

from django.conf import settings

# legacy code

service_codes = {
    100: "Смс-сообщение успешно отправлено.",
    200: "Неправильный api_id",
    201: "Не хватает средств на лицевом счету",
    202: "Неправильно указан получатель",
    203: "Нет текста сообщения",
    204: "Имя отправителя не согласовано с администрацией",
    205: "Сообщение слишком длинное (превышает 8 СМС)",
    206: "Будет превышен или уже превышен дневной лимит на отправку сообщений",
    207: "На этот номер (или один из номеров) нельзя отправлять сообщения, либо"
         " указано более 100 номеров в списке получателей",
    208: "Параметр time указан неправильно",
    209: "Вы добавили этот номер (или один из номеров) в стоп-лист",
    210: "Используется GET, где необходимо использовать POST",
    211: "Метод не найден",
    220: "Сервис временно недоступен, попробуйте чуть позже.",
    300: "Неправильный token (возможно истек срок действия, либо ваш IP изменился)",
    301: "Неправильный пароль, либо пользователь не найден",
    302: "Пользователь авторизован, но аккаунт не подтвержден"
         " (пользователь не ввел код, присланный в регистрационной смс)",
}


def send_sms(msg=None, to=None):
    params = {
        'api_id': settings.SMS_TOKEN,
        'from': 'SC.Check',
        'to': to,
        'text': msg,
        'json': 1
    }
    url = 'http://sms.ru/sms/send'
    response = requests.get(url, params=params)
    response.raise_for_status()
    data_from_service = response.json()
    if 'status_code' in data_from_service and data_from_service['status_code'] in service_codes:
        return service_codes.get(data_from_service['status_code'])


def phone_validate(phone):
    if len(phone) > 11 or len(phone) < 10:
        return False

    phone = ''.join(filter(str.isdigit, phone))
    if len(phone) == 10:
        phone = '7' + phone
    if len(phone) == 11 and phone[0] == '8':
        phone = f'{7}{phone[1:11]}'
    return phone
