from django.http.response import HttpResponse
from pickle import TRUE
from unicodedata import category
from django.shortcuts import render
from .models import staff, Category, Sponsors,Carousel,managestaff,gallery,homeintro, teams



data={
    "personel":[
        {
        "id":1,
        "name":"emre durak",
        "task":"project manager",
        "image":"10.jpg",
        "is_active":True,
         },
            {
        "id":2,
        "name":"murat sağın",
        "task":"machine engineer",
        "image":"10.jpg",
        "is_active":True,
         },
            {
        "id":3,
        "name":"fatih terim",
        "task":"software developer",
        "image":"10.jpg",
        "is_active":True,
         }



    ]
}
# Create your views here.
def index(request):
    sponsors=Sponsors.objects.all()
    obj=Carousel.objects.all()
    galeri=gallery.objects.all()
    homegiris=homeintro.objects.all()
    takim=teams.objects.all()

    context={
        "sponsors":sponsors,
        "obj":obj,
        "galeri":galeri,
        "homegiris":homegiris,
        "takim":takim


    }
    return render(request,"home.html",context)

def about(request):
    teamss=Category.objects.all()
    takim=teams.objects.all()
    context={
        "teams":teamss,
        "persons":managestaff.objects.filter(is_active=True),
        "takim":takim

    }
    return render(request,"about.html",context)

def team(request):
    context={
        "persons":staff.objects.filter(is_active=True),
        "categories":Category.objects.all(),
        "takim":teams.objects.all()

    }
    return render(request,"team.html",context)


def team_details(request,slug):
    team=staff.objects.get(slug=slug)
    return render(request,"team-detail.html",{
        "team":team,
        "person":staff.objects.get(slug=slug)
    })


def manageteam_details(request,slug):
    team=managestaff.objects.get(slug=slug)
    takim=teams.objects.all()

    return render(request,"manageteam-detail.html",{
        "team":team,
        "person":managestaff.objects.get(slug=slug),
         "takim":takim,
    })    

def staff_by_category(request,slug):
    context={
        "persons":Category.objects.get(slug=slug).staff_set.filter(is_active=True),
        # "persons":staff.objects.filter(is_active=True,category__slug=slug),
        "categories":Category.objects.all(),
        "selected_category":slug
    }
    return render(request,"team.html",context)
        







        




def contact(request):
    return render(request,"contact.html")
# def team_detail(request,slug):
#     return render(request,"team-detail.html",{
#         "slug":slug
#     })   


# def team_detail(request, id):
#     return HttpResponse ("blog details: " + str(id))