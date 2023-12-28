from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# this is a dict
monthy_challenges = {
    "january": "Eat no meat",
    "febuary": "Run",
    "march": "Eat no meat",
    "april": "Run",
    "may": "Eat no meat",
    "june": "Run",
    "july": "Eat no meat",
    "august": "Run",
    "september": "Eat no meat",
    "october": "Eat no meat",
    "november": "Run",
    "december": "Run",
}


def index(request):
    months = list(monthy_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthy_challenge(request, month):
    try:
        challenge_text = monthy_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month": month})
    except:
        return HttpResponseNotFound("<h1>whoopsy</h1>")


def monthy_challenge_by_number(request, month):
    months = list(monthy_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month {month}'.format(month=month))
    redirect_month = months[month - 1]

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
