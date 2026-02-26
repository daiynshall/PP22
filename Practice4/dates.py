from datetime import datetime, date, timedelta

# 1) создать дату и время
d = date(2026, 2, 26)
dt = datetime(2026, 2, 26, 10, 30, 0)
print("date:", d)
print("datetime:", dt)

# 2) форматирование (strftime)
print(dt.strftime("%d.%m.%Y %H:%M"))

# 3) разница во времени (timedelta)
dt2 = datetime(2026, 3, 1, 10, 30, 0)
diff = dt2 - dt
print("diff days:", diff.days)

# 4) прибавить дни
print("plus 7 days:", d + timedelta(days=7))

# 5) ISO формат (полезно для API)
print("iso:", dt.isoformat())
