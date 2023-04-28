from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Case, When


def product_list(request, category_slug=None):
    category = None
    # categories = Category.objects.all()

    category_names = ['Супы', 'Завтрак', 'Минеральная вода', 'Римская пицца', ]
    products = Product.objects.filter(available=True).order_by('category__name')
   
    categories = Category.objects.filter(name__in=category_names).order_by(
    Case(
        *[When(name=name, then=pos) for pos, name in enumerate(category_names)]
    )
)
    sorted_products = sorted(products, key=lambda x: category_names.index(x.category.name))

    name_of_category1 = 'Минеральная вода'
    name_of_category2 = 'Минеральная вода'
    cat_prod1 = Product.objects.filter(category__name=name_of_category1)
    cat_prod2 = Product.objects.filter(category__name=name_of_category2)
    if category_slug:
       category = get_object_or_404(Category, slug=category_slug)
       products = products.filter(category=category)
    cart_product_form = CartAddProductForm()

    # if product.category:
    #     category_name = product.category.name
    # else:
    #     category_name = "No category"

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'sorted_products': sorted_products,
                   'products': products,
                   'cat_prod1': cat_prod1,
                   'cat_prod2': cat_prod2,
                   'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})