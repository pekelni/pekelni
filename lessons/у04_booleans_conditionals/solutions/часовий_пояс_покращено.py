import time

СЕКУНД_У_ХВИЛИНІ = 60
ХВИЛИН_У_ГОДИНІ = 60
ГОДИН_У_ДОБІ = 24

зміщення_часового_поясу = int(input('Введіть зміщення часового поясу у годинах: '))
усього_хвилин = int(time.time()) // СЕКУНД_У_ХВИЛИНІ

поточні_хвилини = усього_хвилин % ХВИЛИН_У_ГОДИНІ
усього_годин = усього_хвилин // ХВИЛИН_У_ГОДИНІ
усього_годин += зміщення_часового_поясу
почні_години = усього_годин % ГОДИН_У_ДОБІ

відформатований_час = str(почні_години) + ' годин ' + str(поточні_хвилини) + ' хвилин'
if зміщення_часового_поясу == 3:
    print('У Львові сонячно, ' + відформатований_час)
elif зміщення_часового_поясу == -7:
    print('У Каліфорнії ' + відформатований_час)
else:
    print('Час у часовому поясі ' + str(зміщення_часового_поясу) + ' становить ' + відформатований_час)
