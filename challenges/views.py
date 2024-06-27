from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "January challenge",
    "february": "February challenge",
    "march": "March challenge",
    "april": "April challenge",
    "may": "May challenge",
    "june": "June challenge",
    "july": "July challenge",
    "august": "August challenge",
    "september": "September challenge",
    "october": "October challenge",
    "november": "November challenge",
    "december": "December challenge",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_num(request, month_int):
    months = list(monthly_challenges.keys())

    if month_int > len(months):
        return HttpResponseNotFound("Not a valid month number")
    else:
        redirect_month = months[month_int - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        month_val = monthly_challenges.get(month)
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "challenge_text": month_val,
        })
    except:
        HttpResponseNotFound("<h1>Error</h1>")
