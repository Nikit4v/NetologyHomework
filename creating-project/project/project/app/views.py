from django.shortcuts import render
from app.models import Station, Route
from django.http import HttpResponse


def home_view(request):
    route = request.GET.get("route")
    print(route)
    print(Station.objects.order_by("longitude").filter(route_numbers__name__contains=route)[0].longitude)
    template = "stations.html"
    if route is None:
        return HttpResponse("Ошибка")
    print("-")
    center = {
        "y": Station.objects.order_by("longitude").filter(route_numbers__name__contains=route)[0].longitude/Station.objects.order_by("longitude").filter(route_numbers__name__contains=route)[-1].longitude,
        "x": Station.objects.order_by("latitude").filter(route_numbers__name__contains=route)[0].latitude / Station.objects.order_by("latitude").filter(route_numbers__name__contains=route)[-1].latitude
    }
    print(center)
    context = {
        "stations": Station.objects.all().filter(route_numbers=route),
        "center": center,
        "routes": Route.objects.all().filter(route_numbers=route)
    }
    return render(request, template, context=context)
