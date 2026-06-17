from django.shortcuts import render
from .models import Product, Category, Tag

def product_list(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category')
    tags_filter = request.GET.getlist('tags')
    tags_filter = [t for t in tags_filter if t]  # Remove empty tag values
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__icontains=search_query)
    
    if category_filter:
        products = products.filter(category__id=category_filter)
    
    # if multiple tags are selected, we want to filter products that have all selected tags
    if tags_filter:
        for tag_id in tags_filter:
            products = products.filter(tags__id=tag_id)

    products = products.distinct()

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'search': search_query,
        'selected_category': category_filter,
        'selected_tags': tags_filter,
    }
    return render(request, 'product_list.html', context)
