


def calculate_total_sales(sales_list):
    summa = 0
    for key in sales_list:
        summ = key["quantity"] * key["price_per_unit"]
        summa +=summ

        # TODO Вычислите общую стоимость проданных товаров из списка `sales_list`
    return summa

sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]

total_sales = calculate_total_sales(sales_data)  # TODO Вызовете функцию calculate_total_sales и передайте в функцию значение переменной sales_data
print(f"Общая стоимость проданных товаров: {total_sales}")
