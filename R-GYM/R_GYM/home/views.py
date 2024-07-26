from django.shortcuts import render, HttpResponse
from customadmin.models import admin_class, admin_timetable, admin_trainer, admin_category, admin_product, admin_package
from .models import order

def index(request):
    fetch_class = admin_class.objects.all()
    fetch_table = admin_timetable.objects.all()
    fetch_trainer = admin_trainer.objects.all()
    fetch_package = admin_package.objects.all()
    return render(request, 'index.html', {'fetch_class': fetch_class, 'fetch_table': fetch_table, 'fetch_trainer': fetch_trainer, 'fetch_package': fetch_package})

def about(request):
    fetch_trainer = admin_trainer.objects.all()
    return render(request, 'about-us.html', { 'fetch_trainer': fetch_trainer})

def classes(request):
    fetch_class = admin_class.objects.all()
    return render(request, 'classes.html', {'fetch_class': fetch_class})

def classes_single(request):
    if request.method == "GET":
        class_id = request.GET.get('class-id')
        fetch_class = admin_class.objects.filter(class_id = class_id)
        fetch_trainer = admin_trainer.objects.all()
        return render(request, 'classes-single.html', {'fetch_class': fetch_class, 'fetch_trainer': fetch_trainer})

def classes_timetable(request):
    fetch_table = admin_timetable.objects.all()
    return render(request, 'classes-timetable.html', {'fetch_table': fetch_table})

def our_trainers(request):
    fetch_trainer = admin_trainer.objects.all()
    return render(request, 'our-trainers.html', {'fetch_trainer': fetch_trainer})

def trainers_single(request):
    if request.method == "GET":
        trainer = request.GET.get('trainer_id')
        fetch_trainer = admin_trainer.objects.filter(trainer_id = trainer)
        return render(request, 'trainers-single.html', {'fetch_trainer': fetch_trainer})

def services(request):
    fetch_package = admin_package.objects.all()
    return render(request, 'services.html', {'fetch_package': fetch_package})

def contact_us(request):
    return render(request, 'contact-us.html')

def gallery(request):
    return render(request, 'gallery.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def shop(request):
    fetch_category = admin_category.objects.all()
    fetch_product = admin_product.objects.all()
    return render(request, 'shop.html', {'fetch_category': fetch_category, 'fetch_product': fetch_product})

def shop_single(request):
    if request.method == "GET":
        product_id = request.GET.get('product-id')
        fetch_product = admin_product.objects.filter(product_id = product_id)
        return render(request, 'shop-single.html', {'fetch_product': fetch_product})

def shop_checkout(request):
    if request.method == "GET":
        product_id = request.GET.get('product-id')
        fetch_product = admin_product.objects.filter(product_id = product_id)
        return render(request, 'shop-checkout.html', {'fetch_product': fetch_product})

def thank_you(request):
    if request.method == "POST":
        first_name = request.POST['fn']
        last_name = request.POST['ln']
        user_country = request.POST['country']
        user_address = request.POST['address']
        user_zip = request.POST['zip-code']
        user_phone = request.POST['phone-number']
        user_email = request.POST['email']
        product_id = request.POST['product_id']
        product_name = request.POST['product_name']
        total_price = request.POST['total']
        order_status = request.POST['status']
        order(user_name=first_name + last_name, user_country=user_country, user_address=user_address, user_zip=user_zip, user_phone=user_phone, user_email=user_email, product_id=product_id, product_name=product_name, total_price=total_price, order_status=order_status).save()
        return render(request, 'index.html')