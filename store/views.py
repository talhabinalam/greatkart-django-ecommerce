from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating, ProductGallery
from category.models import Category
from carts.models import CartItem
from orders.models import OrderProduct
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ReviewFrom
from django.contrib import messages
from .models import Account


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()

    in_cart = {}
    cart_id = _cart_id(request)
    cart_items = CartItem.objects.filter(cart__cart_id=cart_id)
    for item in cart_items:
        in_cart[item.product_id] = True

    context = {
        'products': paged_product,
        'product_count': product_count,
        'in_cart': in_cart,
    }
    
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
        
    except Exception as e:
        raise e
    
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None
        
    # Getting the reviews
    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    reviewers = Account.objects.filter(reviewrating__product_id=product.id).distinct()
    
    # Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=product.id)
    
    context = {
        'product': product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'reviewers': reviewers,
        'product_gallery': product_gallery,
    }
    
    return render(request, 'store/product_detail.html', context)


# Search functionality
def search(request):
    products = []
    product_count = 0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewFrom(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewFrom(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)