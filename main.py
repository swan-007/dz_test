geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def f_geo_logs(geo_logs):
    for i in geo_logs:
        for key, val in i.items():
            if "Россия" in val:
                return i



def f_ids(ids):
    list_1 = []
    for val in ids.values():
        for val_str in val:
            list_1.append(val_str)
    list_2 = list(set(list_1))
    return list_2


def f_stats(stats):
    res = max(stats, key=stats.get)
    return res




