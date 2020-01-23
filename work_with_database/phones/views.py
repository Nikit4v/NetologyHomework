from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == "name":
        phone_list = Phone.objects.order_by("name")
    elif sort == "min_price":
        phone_list = Phone.objects.order_by("price")
    else:
        phone_list = Phone.objects.all()
    context = {"list": phone_list}
    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.all()
    template = 'product.html'
    context = {"phone": phones.filter(slug=slug)}
    x=phones.filter(slug=slug)
    print(x[0].name)
    context = {"phone": x[0]}
    return render(request, template, context)
