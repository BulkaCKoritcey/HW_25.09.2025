menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

def menu_sort_by_name():
    sorted_by_name = sorted(menu.items(), key = lambda n: n[0])
    for name, price in sorted_by_name:
        print(name, price)

def menu_sort_by_price():
    sorted_by_price = sorted(menu.items(), key = lambda p: p[1])
    for name, price in sorted_by_price:
        print(name, price)

def mid_price():
    mid = sum(map(lambda x: x[1], menu.items())) / len(menu)
    print(mid)

def add_dish(name, price):
    menu.update({name: price})

def remove_dish(name):
    print("Блюдо удалено" if name in menu else "Блюдо не найдено")
    menu.pop(name, None)

def cheaper_dish(price):
    try:
        cheaper = list(filter(lambda x: x[1] < price, menu.items()))
        print(f"блюда дешевле {price}:")
        for name, price in cheaper:
            print(name, price)
    except:
        print("Ошибка ввода")

def min_max_price():
    cheapest = min(menu.items(), key = lambda x: x[1])
    most_expensive = max(menu.items(), key = lambda x: x[1])
    print(f"Самое дешевое блюдо: {cheapest[0]} {cheapest[1]}")
    print(f"Самое дорогое блюдо: {most_expensive[0]} {most_expensive[1]}")

def show_drinks_sorted():
    drinks = ["coffee", "tea", "juice"]
    drinks_menu = list(filter(lambda x: x[0] in drinks, menu.items()))
    sorted_drinks = sorted(drinks_menu, key=lambda x: x[1])
    print("Напитки:")
    for item, price in sorted_drinks:
        print(f"{item}: {price}")

def order():
    order_input = input().strip()
    order_items = list(map(lambda x: x.strip().lower(), order_input.split(',')))
    
    items = list(filter(lambda x: x in menu, order_items))
    
    order = {item: menu[item] for item in items}
    
    if not any(order):
        print("Вы ничего не выбрали")
        return
    
    total = reduce(lambda x, y: x + y, order.values(), 0)
    
    print("\nВаш заказ:")
    list(map(lambda x: print(f"{x[0]+1}. {x[1][0].capitalize()} — {x[1][1]} руб."), 
             enumerate(order.items())))
    print(f"Итого: {total} руб.")
    











































































