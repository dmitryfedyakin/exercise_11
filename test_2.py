from solution_2 import Product, Basket

bask = Basket()
bask.load_country_codes("country_codes.txt")

while True:
    print("\nМеню:")
    print("1. Загрузить товары из файла")
    print("2. Добавить товар в корзину")
    print("3. Удалить товар из корзины")
    print("4. Показать корзину")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        filename = input("Введите имя файла с товарами: ")
        bask.load_products_from_file(filename)
        print("Товары загружены.")
        
    elif choice == '2':
        ean_code = input("Введите штрих-код товара: ")
        product = bask.find_product(ean_code)
        if product:
            quantity = int(input("Введите количество: "))
            bask.add_item(product, quantity)
            print("Товар добавлен в корзину.")
        else:
            print("Товар не найден.")

    elif choice == '3':
        ean_code = input("Введите штрих-код товара: ")
        product = bask.find_product(ean_code)
        if product:
            quantity = int(input("Введите количество: "))
            bask.remove_item(product, quantity)
            print("Товар удален из корзины.")
        else:
            print("Товар не найден.")
            
    elif choice == '4':
        print("Содержимое корзины:")
        for ean_code, quantity in bask.get_items().items():
            product = bask.find_product(ean_code)
            if product:
                country = product.country_code
                country_info = f" ({country})" if country else ""
                print(f"- {product.get_name()} ({ean_code}){country_info}: {quantity} шт.")
        print(f"Общая стоимость: {bask.get_total_price()}")

    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор.")
