import csv
import datetime
from collections import defaultdict

import matplotlib.pyplot as plt


# Читаем данные из файла
def load_data(path):
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            date = datetime.datetime.strptime(line[0], "%Y-%m-%d")
            user_id = int(line[1])
            data.append((date, user_id))
    return data


# Группировкой пользователей по дате
def group_by_date(data):
    date_group = defaultdict(set)
    for date, user_id in data:
        date_group[date].add(user_id)
    return date_group


# Вычисляем dau для промежутка в днях и получаем словарь, где ключ - дата, а значение - количество уникальных пользователей в эту дату
def calculate_dau(date_group, end_date, day_step):
    start_date = end_date - datetime.timedelta(days=day_step)
    dau_dict = {date: len(users) for date, users in date_group.items() if date >= start_date}
    return dau_dict


data = load_data('varying_user_activity_data.csv')
end_date = max(date for date, user_id in data)
date_group = group_by_date(data)
day_step = 30
dau_dict = calculate_dau(date_group, end_date, day_step)
# print(calculate_dau(date_group, end_date, day_step)

_, ax = plt.subplots(figsize=(10, 6))

ax.bar(dau_dict.keys(), dau_dict.values())
ax.set_title("DAU for the last 30 days")
ax.set_xlabel("Date")
ax.set_ylabel("DAU")

plt.tight_layout()
plt.show()
