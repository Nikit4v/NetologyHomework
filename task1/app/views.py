import csv
from app.YearClass import Year

from django.shortcuts import render
from django.conf import settings

bgctemplate = "background-color: "


def setBgc(color):
     return f"{bgctemplate}{color};"

def getBgc(value):
    if value != "":
        value = float(value)
        if value < 0:
            return setBgc("green")
        elif value < 1:
            return setBgc("white")
        else:
            if value < 2:
                return setBgc("#ff6666")
            elif value < 5:
                return setBgc("#ff3333")
            else:
                return setBgc('#ff0000')


def inflation_view(request,):
    template_name = 'inflation.html'
    csvfile = open(settings.INFLATION_CSV, encoding="utf-8")
    reader = csv.DictReader(csvfile, delimiter=";")
    years_array = []
    for row in reader:
        year_obj = {"number": {"val": row["Год"]},
                    "j": {"val": row["Янв"], "bgc": getBgc(row["Янв"])},
                    "f": {"val": row["Фев"], "bgc": getBgc(row["Фев"])},
                    "m": {"val": row["Мар"], "bgc": getBgc(row["Мар"])},
                    "a": {"val": row["Апр"], "bgc": getBgc(row["Апр"])},
                    "my": {"val": row["Май"], "bgc": getBgc(row["Май"])},
                    "jn": {"val": row["Июн"], "bgc": getBgc(row["Июн"])},
                    "jl": {"val": row["Июл"], "bgc": getBgc(row["Июл"])},
                    "ag": {"val": row["Авг"], "bgc": getBgc(row["Авг"])},
                    "s": {"val": row["Сен"], "bgc": getBgc(row["Сен"])},
                    "o": {"val": row["Окт"], "bgc": getBgc(row["Окт"])},
                    "n": {"val": row["Ноя"], "bgc": getBgc(row["Ноя"])},
                    "d": {"val": row["Дек"], "bgc": getBgc(row["Дек"])},
                    "all": {"val": row["Суммарная"], "bgc": getBgc(row["Суммарная"])}
                    }
        years_array.append(year_obj)
    context = {
        "years": years_array,
        "months": [
            "year",
            "j",
            "f",
            "m",
            "a",
            "my",
            "jn",
            "jl",
            "ag",
            "s",
            "o",
            "n",
            "d",
            "all"
        ],
        "column_names": ["Год", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь", "Суммарная"]
    }
    return render(request, template_name, context)
