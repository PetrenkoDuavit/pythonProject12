import codecs
import re

# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     # Открываем HTML файл и читаем его содержимое
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#
#     # Удаляем HTML-теги, заменяя их на пустую строку
#     clean_text = re.sub(r'<[^>]*>', '', html)
#
#     # Записываем очищенный текст в новый файл
#     with codecs.open(result_file, 'w', 'utf-8') as output_file:
#         output_file.write(clean_text)




def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        result = []
        for line in file:
            current_text_list = re.findall(r">(.+)</", line)  # <title>Жарт про функції</title>
            if len(current_text_list) > 0:
                result += current_text_list
        print(f"Result: {result}")
        if len(result) > 0:
            with open(result_file, 'w', encoding='utf-8') as new_file:
                new_file.write('\n'.join(result))


delete_html_tags("draft.html")

print( "HW 12.2")
class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self): # возвращаю название товара и цену
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self): # Возвращает имя и фамилию пользователя
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}
        self.total = 0

    def add_item(self, item, cnt): # добавляю товар и его количество
        self.products[item] = cnt

    def get_total(self): # Возвращает сумму покупок
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self): # возвращает инф о пользователях и товарах
        item_list = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{item_list}"


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40