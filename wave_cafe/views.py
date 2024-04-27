from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Reservation_Data
from .models import Franchise_Data
from .models import Contact_Data

# Create your views here.

"""def index(request):
    template = loader.get_template('Index.html')
    return HttpResponse(template.render())"""

def index(request):
    mydata = Franchise_Data.objects.all()
    if (mydata != ""):
        return render(request, "index.html", {"franchise_data":mydata})
    else:
        return render(request, "index.html")
    
def saveData(request):
    if request.method == "POST":
        yname = request.POST["yname"]
        phone = request.POST["phone"]
        mail = request.POST["mail"]
        city = request.POST["city"]
        investment = request.POST["investment"]
        information = request.POST["information"]

        obj = Franchise_Data()
        obj.Name = yname
        obj.Phone = phone
        obj.Mail = mail
        obj.City = city
        obj.Investment = investment
        obj.Information = information
        obj.save()
        mydata = Franchise_Data.objects.all()
        return redirect("index")
    return render(request, "index.html")

def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('Menu.html')
    return HttpResponse(template.render())

"""def reserve(request):
    template = loader.get_template('Reservation.html')
    return HttpResponse(template.render())"""

"""def contact(request):
    template = loader.get_template('Contact.html')
    return HttpResponse(template.render())"""

def reservation(request):
    mydata = Reservation_Data.objects.all()
    if (mydata != ""):
        return render(request, "Reservation.html", {"reservation_data":mydata})
    else:
        return render(request, "Reservation.html")
    
def addData(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        person = request.POST["person"]
        mail = request.POST["mail"]
        date = request.POST["date"]
        time = request.POST["time"]
        phone = request.POST["phone"]
        plan = request.POST["plan"]
        occasion = request.POST["occasion"]
        special = request.POST["special"]

        obj = Reservation_Data()
        obj.Name = fname
        obj.Person = person
        obj.Mail = mail
        obj.Date = date
        obj.Time = time
        obj.Phone = phone
        obj.Plan = plan
        obj.Occasion = occasion
        obj.Special = special
        obj.save()
        mydata = Reservation_Data.objects.all()
        return redirect("reservation")
    return render(request, "Reservation.html")
    
def contact_us(request):
    mydata = Contact_Data.objects.all()
    if (mydata != ""):
        return render(request, "Contact.html", {"contact_data":mydata})
    else:
        return render(request, "Contact.html")
    
def getData(request):
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        obj = Contact_Data()
        obj.Name = name
        obj.Mail = mail
        obj.Phone = phone
        obj.Message = message
        obj.save()
        mydata = Contact_Data.objects.all()
        return redirect("contact_us")
    return render(request, "Contact.html")