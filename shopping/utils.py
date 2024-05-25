from .models import Product


filter_keys = [
    'bracelet', 'pendulum', 'natural_stone', 'incence', 'chakra_stone'
]

sort_options = [
    'date-added-low-to-high', 'date-added-high-to-low',
    'price-low-to-high', 'price-high-to-low',
    'name-a-z', 'name-z-a'
]


def get_filter_key_values(post_data) -> list:
    sent_keys = [post_data.get(key) for key in filter_keys]
    return list(filter(lambda key: post_data.get(key) is not None, sent_keys))


def get_search_results(search_key) -> list:
    return Product.objects.filter(name__icontains=search_key).all()


def get_filter_results(filter_key_values) -> list:
    product_list = list(Product.objects.all())
    filter_results = []
    for k in filter_key_values:
        filter_results += list(
            filter(lambda p: p.category.lower() == k.lower(), product_list))
    return filter_results


def sort_products(order_by) -> list:
    product_list = list(Product.objects.all())
    if order_by == 'price-low-to-high':
        return sorted(product_list, key=lambda p: p.price)
    elif order_by == 'price-high-to-low':
        return sorted(product_list, key=lambda p: p.price, reverse=True)
    elif order_by == 'name-a-z':
        return sorted(product_list, key=lambda p: p.name)
    elif order_by == 'name-z-a':
        return sorted(product_list, key=lambda p: p.name, reverse=True)
    else:
        return []


def get_empty_filters() -> dict:
    return {key: False for key in filter_keys}


def get_filter_values(filter_results) -> dict:
    filter_values = get_empty_filters()
    for product in filter_results:
        filter_values[product.category] = True
    return filter_values
