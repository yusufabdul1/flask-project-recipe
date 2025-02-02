from flask import request, jsonify
from models import db, Recipe, Ingredient, FavoriteRecipe, RecipeIngredient

def init_app(app):
    # Recipe Routes
    @app.route('/recipes', methods=['GET'])
    def get_recipes():
        recipes = Recipe.query.all()
        return jsonify([recipe.serialize() for recipe in recipes])

    @app.route('/recipes', methods=['POST'])
    def add_recipe():
        data = request.get_json()
        new_recipe = Recipe(
            title=data['title'],
            description=data['description'],
            instructions=data['instructions'],
            meal_type=data['meal_type']
        )
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify(new_recipe.serialize()), 201

    @app.route('/recipes/<int:id>', methods=['PUT'])
    def update_recipe(id):
        data = request.get_json()
        recipe = Recipe.query.get(id)
        if not recipe:
            return jsonify({'error': 'Recipe not found'}), 404
        recipe.title = data['title']
        recipe.description = data['description']
        recipe.instructions = data['instructions']
        recipe.meal_type = data['meal_type']
        db.session.commit()
        return jsonify(recipe.serialize())

    @app.route('/recipes/<int:id>', methods=['DELETE'])
    def delete_recipe(id):
        recipe = Recipe.query.get(id)
        if not recipe:
            return jsonify({'error': 'Recipe not found'}), 404
        db.session.delete(recipe)
        db.session.commit()
        return '', 204

    # Ingredient Routes
    @app.route('/ingredients', methods=['GET'])
    def get_ingredients():
        ingredients = Ingredient.query.all()
        return jsonify([ingredient.serialize() for ingredient in ingredients])

    @app.route('/ingredients', methods=['POST'])
    def add_ingredient():
        data = request.get_json()
        new_ingredient = Ingredient(name=data['name'])
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify(new_ingredient.serialize()), 201

    @app.route('/ingredients/<int:id>', methods=['DELETE'])
    def delete_ingredient(id):
        ingredient = Ingredient.query.get(id)
        if not ingredient:
            return jsonify({'error': 'Ingredient not found'}), 404
        db.session.delete(ingredient)
        db.session.commit()
        return '', 204

    # Favorite Recipe Routes
    @app.route('/favorites', methods=['GET'])
    def get_favorites():
        favorites = FavoriteRecipe.query.all()
        return jsonify([favorite.serialize() for favorite in favorites])

    @app.route('/favorites', methods=['POST'])
    def add_favorite():
        data = request.get_json()
        new_favorite = FavoriteRecipe(recipe_id=data['recipe_id'])
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify(new_favorite.serialize()), 201

    @app.route('/favorites/<int:id>', methods=['DELETE'])
    def delete_favorite(id):
        favorite = FavoriteRecipe.query.get(id)
        if not favorite:
            return jsonify({'error': 'Favorite not found'}), 404
        db.session.delete(favorite)
        db.session.commit()
        return '', 204

    # Recipe Ingredient Routes
    @app.route('/recipe_ingredients', methods=['GET'])
    def get_recipe_ingredients():
        recipe_ingredients = RecipeIngredient.query.all()
        return jsonify([recipe_ingredient.serialize() for recipe_ingredient in recipe_ingredients])

    @app.route('/recipe_ingredients', methods=['POST'])
    def add_recipe_ingredient():
        data = request.get_json()
        new_recipe_ingredient = RecipeIngredient(
            recipe_id=data['recipe_id'],
            ingredient_id=data['ingredient_id']
        )
        db.session.add(new_recipe_ingredient)
        db.session.commit()
        return jsonify(new_recipe_ingredient.serialize()), 201

    @app.route('/recipe_ingredients/<int:id>', methods=['DELETE'])
    def delete_recipe_ingredient(id):
        recipe_ingredient = RecipeIngredient.query.get(id)
        if not recipe_ingredient:
            return jsonify({'error': 'Recipe Ingredient not found'}), 404
        db.session.delete(recipe_ingredient)
        db.session.commit()
        return '', 204