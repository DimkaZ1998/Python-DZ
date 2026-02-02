import random
from datetime import datetime, timedelta

def total_revenue(sales):
    return sum(item['price'] * item['quantity'] for item in sales)

def best_selling_product(sales):
    product_sales = {}
    for item in sales:
        product_sales[item['product']] = product_sales.get(item['product'], 0) + item['quantity']
    if not product_sales:
        return None
    return max(product_sales, key=product_sales.get)

def best_seller(sales):
    seller_revenue = {}
    for item in sales:
        revenue = item['price'] * item['quantity']
        seller_revenue[item['seller']] = seller_revenue.get(item['seller'], 0) + revenue
    if not seller_revenue:
        return None
    return max(seller_revenue, key=seller_revenue.get)

def sales_by_category(sales):
    category_revenue = {}
    for item in sales:
        revenue = item['price'] * item['quantity']
        category_revenue[item['category']] = category_revenue.get(item['category'], 0) + revenue
    return category_revenue

def daily_sales(sales):
    daily_revenue = {}
    for item in sales:
        date = item['date']
        revenue = item['price'] * item['quantity']
        daily_revenue[date] = daily_revenue.get(date, 0) + revenue
    return daily_revenue

def add_sale(sales, new_sale):
    required_fields = {'date', 'product', 'category', 'price', 'quantity', 'seller'}
    if not required_fields.issubset(new_sale):
        raise ValueError("Неполные данные для продажи")
    # Можно добавить дополнительные проверки типов, формата даты, цен и т.д.
    sales.append(new_sale)

def generate_sample_data(num_records):
    products = ['Ноутбук', 'Мышь', 'Клавиатура', 'Телевизор', 'Смартфон']
    categories = ['Электроника', 'Бытовая техника', 'Офисные товары']
    sellers = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов']
    start_date = datetime(2024, 1, 1)
    sales = []

    for _ in range(num_records):
        days_offset = random.randint(0, 30)
        date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')
        product = random.choice(products)
        category = random.choice(categories)
        price = random.randint(500, 100000)
        quantity = random.randint(1, 10)
        seller = random.choice(sellers)
        sales.append({
            'date': date,
            'product': product,
            'category': category,
            'price': price,
            'quantity': quantity,
            'seller': seller
        })
    return sales

def generate_report(sales, start_date, end_date):
    report_sales = [s for s in sales if start_date <= s['date'] <= end_date]
    total = total_revenue(report_sales)
    products = best_selling_product(report_sales)
    seller = best_seller(report_sales)
    return {
        'total_revenue': total,
        'best_product': products,
        'best_seller': seller
    }

# Пример использования
sales = generate_sample_data(50)

print(f"Общая выручка: {total_revenue(sales)} руб.")
print(f"Лучший товар: {best_selling_product(sales)}")
print(f"Лучший продавец: {best_seller(sales)}")
print("Выручка по категориям:", sales_by_category(sales))
print("Продажи по дням:", daily_sales(sales))