from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns_returns_list_of_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(b, Bun) for b in buns)

    def test_available_ingredients_returns_list_of_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(i, Ingredient) for i in ingredients)

    def test_buns_have_expected_names(self):
        db = Database()
        names = [bun.get_name() for bun in db.buns]
        assert names == ["black bun", "white bun", "red bun"]

    def test_ingredients_have_expected_names_and_types(self):
        db = Database()
        expected = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce"),
            (INGREDIENT_TYPE_SAUCE, "sour cream"),
            (INGREDIENT_TYPE_SAUCE, "chili sauce"),
            (INGREDIENT_TYPE_FILLING, "cutlet"),
            (INGREDIENT_TYPE_FILLING, "dinosaur"),
            (INGREDIENT_TYPE_FILLING, "sausage")
        ]
        actual = [(i.get_type(), i.get_name()) for i in db.ingredients]
        assert actual == expected