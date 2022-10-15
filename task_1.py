src = not False and True or False and not True

# results = True and True or False and False # избавляемся от отрицания
# results = True or False # избавляемся от логического "И"
# results = True # избавляемся от логического "ИЛИ"


result = True

print(src == result)
