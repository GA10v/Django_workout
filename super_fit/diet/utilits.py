from .models import Food


class FoodDemo:
    def __init__(self):
        self.all_food = Food.objects.all