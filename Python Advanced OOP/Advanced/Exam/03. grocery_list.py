def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []
    groceries_left = grocery_list.copy()

    for product, price in args:
        if product not in bought_products and product in grocery_list:
            if price <= budget:
                bought_products.append(product)
                groceries_left.remove(product)
                budget -= float(price)
            else:
                break

    if not groceries_left:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(groceries_left)}"


