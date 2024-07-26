from django.shortcuts import render
from django.http import HttpResponse
from .models import admin_category, admin_product, admin_package, admin_trainer, admin_class, admin_timetable
from home.models import order
def dashboard(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email=="Admin@gmail.com":
            if password=="Admin":
                return render(request, 'dashboard.html')
            else:
                return HttpResponse("Invalid Login")
        else:
            return HttpResponse("Invalid Login")

def product(request):
    fetchdata = admin_product.objects.all()
    fetchcat = admin_category.objects.all()
    return render(request, 'product.html', {'data': fetchdata, 'catdata': fetchcat})

def packages(request):
    fetch_package = admin_package.objects.all()
    return render(request, 'admin-packages.html', {'fetch_package': fetch_package})

def trainer(request):
    fetch_trainer = admin_trainer.objects.all()
    return render(request, 'admin-trainer.html', {'fetch_trainer': fetch_trainer})

def add_class(request):
    fetch_class = admin_class.objects.all()
    return render(request, 'add-class.html', {'fetch_class': fetch_class})

def time_table(request):
    fetch_timetable = admin_timetable.objects.all()
    fetch_class = admin_class.objects.all()
    return render(request, 'admin-time-table.html', {'fetch_timetable': fetch_timetable, 'fetch_class': fetch_class})

def pending_order(request):
    fetch_order = order.objects.all()
    return render(request, 'pending-order.html', {'fetch_order': fetch_order})

def completed_order(request):
    return render(request, 'completed-order.html')

def contact(request):
    return render(request, 'admin-contact.html')

def cat(request):
    if request.method == "POST":
        cat_name = request.POST['cat-name']
        cat_image = request.FILES['cat-image']
        admin_category(cat_name=cat_name, cat_image=cat_image).save()
        return HttpResponse()

def pro(request):
    if request.method == "POST":
        product_name = request.POST['product-name']
        product_category = request.POST['product-category']
        product_price = request.POST['product-price']
        product_quantity = request.POST['product-quantity']
        product_tag = request.POST['product-tag']
        product_image = request.FILES['product-image']
        product_short_description = request.POST['product-short-description']
        product_information = request.POST['product-information']
        product_description = request.POST['product-description']
        admin_product(product_name=product_name, product_category=product_category, product_price=product_price, product_quantity=product_quantity, product_tag=product_tag, product_image=product_image, product_short_description=product_short_description, product_information=product_information, product_description=product_description).save()
        return HttpResponse()

def pack(request):
    if request.method == 'POST':
        package_name = request.POST['package-name']
        package_duration = request.POST['package-duration']
        package_price = request.POST['package-price']
        package_image = request.FILES['package-image']
        package_specification = request.POST['package-specification']
        package_description = request.POST['package-description']
        admin_package(package_name=package_name, package_duration=package_duration, package_price=package_price, package_image=package_image.name, package_specification=package_specification, package_description=package_description).save()
        return HttpResponse()

def train(request):
    if request.method == 'POST':
        trainer_name = request.POST['trainer-name']
        trainer_type = request.POST['trainer-type']
        trainer_speciality = request.POST['trainer-speciality']
        trainer_image = request.FILES['trainer-image']
        trainer_description = request.POST['trainer-description']
        admin_trainer(trainer_name=trainer_name, trainer_type=trainer_type, trainer_speciality=trainer_speciality, trainer_image=trainer_image, trainer_description=trainer_description).save()
        return HttpResponse()

def class_data(request):
    if request.method == 'POST':
        class_name = request.POST['class-name']
        class_title = request.POST['class-title']
        class_description = request.POST['class-description']
        class_benefits = request.POST['class-benefit']
        class_image = request.FILES['class-image']
        admin_class(class_name=class_name, class_title=class_title, class_description=class_description, class_benefits=class_benefits, class_image=class_image).save()
        return HttpResponse()

def add_time_tale(request):
        if request.method == 'POST':
            timetable_class = request.POST['class-name']
            timetable_day = request.POST['day']
            timetable_starttime = request.POST['start-time']
            timetable_endtime = request.POST['end-time']
            admin_timetable(timetable_class=timetable_class, timetable_day=timetable_day, timetable_starttime=timetable_starttime, timetable_endtime=timetable_endtime).save()
            return HttpResponse()

def order_completed(request):
    if request.method == "POST":
        order_completed = request.POST["order_status"]
        order_id = request.POST["order_id"]
        order.objects.filter(order_id=order_id).update(order_status=order_completed)
        return HttpResponse("Updated")