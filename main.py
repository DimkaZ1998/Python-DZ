class Product:
    """Класс для представления товара в магазине"""
    next_id = 1 # Количество видов продуктов

    def __init__(self, name, price, quantity):
        if price <= 0: # Если цена отрицательная - выводим ошибку
            raise ValueError("Цена должна быть положительной")
        if quantity < 0: # Если количество товаров меньше нуля - ошибка
            raise ValueError("Количество не может быть отрицательным")
        
        self.id = Product.next_id # Уникальный id товара
        Product.next_id += 1 # После создания продукта увеличиваем его id

        # Если ничего не вызвало ошибку - присваиваем полям значения
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_quantity(self, amount): # Уменьшение количества товаров на складе
        if amount > self.quantity: # Если число товаров для уменьшения больше самого количества товаров - ошибка
            raise ValueError(f"Недостаточно товара. Доступно: {self.quantity}")
        if amount <= 0: # Если число для уменьшения количества товаров <= 0 - ошибка
            raise ValueError("Количество должно быть положительным")
        
        # Если ничего не вызвало ошибку - уменьшаем количество товара на складе
        self.quantity -= amount

    def __str__(self):
        return f"{self.name} - {self.price} руб. (осталось: {self.quantity})" # Информация о конкретном товаре

class Customer:
    """Класс для представления покупателя"""
    def __init__(self, name, email, initial_balance=0): # Укажем баланс по умолчанию - 0
        if initial_balance < 0: # Если введен отрицательный баланс - ошибка
            raise ValueError("Баланс не может быть отрицательным")
        
        # Если баланс введен корректно - инициализируем покупателя
        self.name = name
        self.email = email
        self._balance = initial_balance
        self.orders = [] # История покупок

    def add_money(self, amount):
        """Пополнение баланса"""
        if amount <= 0: # Невозможно поплнить баланс на отрицательное число
            raise ValueError("Сумма пополнения должна быть положительной")
        
        # Если сумма введена корректно - пополняем баланс
        self._balance += amount
        print(f"{self.name}: пополнено {amount} руб. Новый баланс: {self._balance}") # Лог событий

    def charge(self, amount):
        """Списание баланса"""
        if amount <= 0: # Невозможно списать отрицательное количество денег
            raise ValueError("Сумма списания должна быть положительной")
        if amount > self._balance: # Если сумма списания больше самого баланса - ошибка
            raise ValueError("На счете недостаточно средств для списания")
        
        # Если сумма введена корректно - списываем деньги
        self._balance -= amount
        return True # Флаг, показывающий успешность операции
    
    def get_balance(self):
        """Возвращает текущий баланс"""
        return self._balance

    def add_order(self, order): # Объект класса Order
        """Добавляет заказ в историю"""
        self.orders.append(order)

    def __str__(self):
        return f"{self.name} ({self.email}), баланс: {self._balance} руб." # Информация о пользователе
    
class Cart: # Корзина
    def __init__(self, customer): # Вводим покупателя для данной корзины
        self.customer = customer
        self.items = {} # Сама корзина

    def add_product(self, product, quantity=1): # Добавление продукта в корзину
        if quantity <= 0: # Если введено неположительное количество товара - ошибка
            raise ValueError("Количество должно быть положительным")
        if product.quantity < quantity: # Если товара недостаточно на складе - ошибка
            raise ValueError(f"Недостаточно товара '{product.name}' на складе")
        
        if product.id in self.items: # Если продукт уже есть в корзине - не создаем дубликат, а увеличиваем количество
            self.items[product.id] += quantity
        else: # Если нет - создаем в списке items новую пару ключ : значение (id-продукта : ео количество)
            self.items[product.id] = quantity

        print(f"Добавлено в корзину: {product.name} x{quantity}") # Вывод в лог событий
        
    def remove_product(self, product, quantity=None): # Удаление товара из корзины (если введено кол-во - удаляем конкретное кол-во товаров)
        if product.id not in self.items: # Если нету такого товара в корзине - сообщим об этом пользователю
            print(f"Товар '{product.name}' не найден в корзине")
            return #   Завершим функцию
        
        if quantity is None: # Если пользователь не веел кол-во - полностью удалим товар из корзины
            del self.items[product.id]
            print(f"Товар '{product.name}' полностью удален из корзины")
        else:
            if quantity <= 0: # Если введено неположительное кол-во - ошибка
                raise ValueError("Количество должно быть положительным")
            
            if quantity >= self.items[product.id]: # Если пользователь ввел количество товара для  удаления, больше, чем товаров в корзине - также полностью удалим товар
                del self.items[product.id]
                print(f"Товар '{product.name}' полностью удален из корзины")
            
            else: # Если количестьо для удаления введено правильно - уменьшим его кол-во
                self.items[product.id] -= quantity
                print(f"Удалено из корзины: {product.name} x{quantity}")

    def get_total(self, products_dict): # Получим сумму всей корзины, product_dict - склад товаров, представленный списком id продукта: object_Product
        total = 0 # Сумма
        for product_id, quantity in self.items.items(): # Пройдемся по списку товаров(id: quantity)
            if product_id in products_dict: # Если товар есть на складе
                product = products_dict[product_id] # Получим продукт и информацию о нем
                total += product.price * quantity # Умножим цену на количество и прибавим к нашей сумме
        return total
    
    def checkout(self, products_dict): # Покупаем корзину, products_dict - склад товаров, представленный списком id продукта: object_Product
        if not self.items: # Если корзина пустая - сообщим пользователю и завершим функцию
            print("Корзина пуста!")
            return None
        
        total = self.get_total(products_dict) # Сумма для списания, перелдаем туда наш склад

        if total > self.customer.get_balance(): # Сообщим польщователю если недостаточно средств
            print(f"Недостаточно средств. Нужно: {total}, доступно: {self.customer.get_balance()}")
            return None
        
        for product_id, quantity in self.items.items(): # Если все в порядке - пройдемся по списку товаров(id: quantity)
            if product_id in products_dict: # Если товар есть на складе 
                product = products_dict[product_id] # Получим товар и информацию о нём
                if product.quantity < quantity: # Если количество товара на складе меньше, чем ввел пользователь - сообщим об этом
                    print(f"Недостаточно товара '{product.name}' на складе")
                    return None
                
        order = Order(self.customer, self.items.copy(), total) # Создадим запись о заказе, его 'чек', где есть сумма, наша корзина и покупателдь

        self.customer.charge(total) # Спишем деньги 

        # Уменьшим количество товаров на скалдке после покупки
        for product_id, quantity in self.items.items():
            if product_id in products_dict: # Если продукт есть на скалде
                product = products_dict[product_id] # Получим продукт
                product.reduce_quantity(quantity) # Уменьшим его количество на количсевто купленных товаров ланного вида

        self.customer.add_order(order) # Добавим заказ в историю покупок

        self.items.clear() # Очистим корзину после успешной покупки

        print(f"Заказ оформлен! Номер заказа: {order.id}") # Сообщим польщователю об успешности операции
        return order # Вернем наш заказ
    
    def show(self, products_dict): # Покажем содержимое корзины
        if not self.items:
            print("Корзина пуста")
            return
        
        print("\nСодержимое корзины:")
        print('-' * 40)

        for product_id, quantity in self.items.items():
            if product_id in products_dict: # Если продукт есть на складе
                product = products_dict[product_id] # Получим продукт
                print(f"{product.name} x{quantity} = {product.price * quantity} руб.") # Информация о данном продукте и уена за корличество товара

        print('-' * 40)
        print(f"Итого: {self.get_total(products_dict)} руб.") # Сумма покупки

class Order: # Заказ
    next_id = 1 # Количество заказов

    def __init__(self, customer, items, total):
        from datetime import datetime # Время заказа
        self.id = Order.next_id # Получим уникальный id
        Order.next_id += 1 # Увеличим корличество

        self.customer = customer
        self.items = items
        self.total = total
        self.date = datetime.now()
        self.status = 'обработан'

    def __str__(self): # Информация о заказе
        items_str = ", ".join([f"товар {pid}: x{qty}" for pid, qty in self.items.items()])
        date_str = self.date.strftime("%Y-%m-%d %H:%M")
        return f"Заказ #{self.id} от {date_str}: {items_str}, сумма: {self.total} руб."
