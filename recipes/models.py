from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def total_nutrition(self):
        total_calories = sum(item.ingredient.calories * item.quantity for item in self.recipeingredient_set.all())
        total_protein = sum(item.ingredient.protein * item.quantity for item in self.recipeingredient_set.all())
        total_carbs = sum(item.ingredient.carbs * item.quantity for item in self.recipeingredient_set.all())
        total_fat = sum(item.ingredient.fat * item.quantity for item in self.recipeingredient_set.all())
        return {
            'calories': total_calories,
            'protein': total_protein,
            'carbs': total_carbs,
            'fat': total_fat,
        }

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"
