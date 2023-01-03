class Item:

    def __init__(self, name, price, decription, demensions):
        self.name = name
        self.price = price
        self.decription = decription
        self.demensions = demensions

    def __str__(self):
        return f'Item: {self.name} at {self.price}$ per pcs (color: {self.decription}/ size: {self.demensions})'


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'Buyer: {self.name} {self.surname} (number: {self.numberphone})'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        name = ''
        for key, cnt in self.products.items():
            name += f'\n\t{key.name}: {cnt} pcs.'
        return f'{self.user.name} {self.user.surname}:{name}'

    def get_total(self):
        total = 0
        for key, cnt in self.products.items():
            total += key.price * cnt
        return f'The price of your items: {total}$'


phone = Item('iPhone 14', 950, "black", "big", )
phone_case = Item('Case from China', 20, "red", "middle", )
laptop = Item('MacBook', 1000, "gold", "middle", )

print(phone)  # lemon, price: 5
print(phone_case)
print(f"{laptop}\n")


buyer_1 = User("Borys", "Oleksiienko", "02628162")
print(buyer_1)  # Borys Oleksiienko

cart_1 = Purchase(buyer_1)
cart_1.add_item(phone, 4)
cart_1.add_item(phone_case, 20)
cart_1.add_item(laptop, 3)
print(cart_1)
print(cart_1.get_total())

buyer_2 = User("Ivan", "Helicopter", "31822710")
print(f"\n{buyer_2}")  # Borys Oleksiienko

cart_2 = Purchase(buyer_2)
cart_2.add_item(phone, 1)
cart_2.add_item(phone_case, 1)
cart_2.add_item(laptop, 1)
print(cart_2)
print(cart_2.get_total())


