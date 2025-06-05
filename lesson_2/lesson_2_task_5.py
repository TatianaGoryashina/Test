def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        return "Зима"
    elif month == 3 or month == 4 or month == 5:
        return "Весна"
    elif month == 6 or month == 7 or month == 8:
        return "Лето"
    elif month == 9 or month == 10 or month == 11:
        return "Осень"
    else:
        return "Укажите правильный номер месяца (от 1 до 12)"


# Примеры использования:
print(month_to_season(2))
print(month_to_season(5))
print(month_to_season(8))
print(month_to_season(11))
print(month_to_season(13))
print(month_to_season(3))
