from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    nutrition = recipe.total_nutrition()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'nutrition': nutrition})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('recipe_list')  # Assuming you have a view named recipe_list
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})