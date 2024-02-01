from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe(request, recipe_name):
    context = {
        'recipe': {key: DATA[recipe_name][key] for key in DATA[recipe_name]}
    }
    return context

def omlet(request):
    servings = int(request.GET.get("servings", 1))
    if servings >= 1:
        context = recipe(request, 'omlet')
        con = context['recipe']
        for key in con:
            con[key] *= servings
        context.update({'recipe': con})
        return render(request, 'calculator/index.html', context)
    else:
        context = recipe(request, 'omlet')
        return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get("servings", 1))
    if servings >= 1:
        context = recipe(request, 'pasta')
        con = context['recipe']
        for key in con:
            con[key] *= servings
        context.update({'recipe': con})
        return render(request, 'calculator/index.html', context)
    else:
        context = recipe(request, 'omlet')
        return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get("servings", 1))
    if servings >= 1:
        context = recipe(request, 'buter')
        con = context['recipe']
        for key in con:
            con[key] *= servings
        context.update({'recipe': con})
        return render(request, 'calculator/index.html', context)
    else:
        context = recipe(request, 'omlet')
        return render(request, 'calculator/index.html', context)
