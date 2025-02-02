from app import app, db
from models import Recipe, Ingredient, FavoriteRecipe, RecipeIngredient

def seed_data():
    with app.app_context():
        db.create_all()

        # Add sample recipes
        recipe1 = Recipe(title="Pancakes", description="Fluffy pancakes", instructions="Mix and cook", meal_type="Breakfast")
        recipe2 = Recipe(title="Salad", description="Fresh salad", instructions="Chop and mix", meal_type="Lunch")
        
        # Add sample ingredients
        ingredient1 = Ingredient(name="Flour")
        ingredient2 = Ingredient(name="Lettuce")

        # Add sample favorite recipes
        favorite1 = FavoriteRecipe(recipe_id=1)

        # Add sample recipe ingredients
        recipe_ingredient1 = RecipeIngredient(recipe_id=1, ingredient_id=1)
        recipe_ingredient2 = RecipeIngredient(recipe_id=2, ingredient_id=2)

        db.session.add_all([recipe1, recipe2, ingredient1, ingredient2, favorite1, recipe_ingredient1, recipe_ingredient2])
        
        db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
    seed_data()