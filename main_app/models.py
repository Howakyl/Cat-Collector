from django.db import models
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#SQL representation of Many-to-Many relationship
# class Cat_Toys:
#     cat = models.ForeignKey(Cat)        
#     toy = models.ForeignKey(Toy)        


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age



# cats = [
#     Cat('Felix' , 'Bombay' , 'troublemaker' , 5),
#     Cat('Fluffy' , 'Himalayan' , 'sleepy' , 2),
#     Cat('Mittens' , 'Siamese' , 'very friendly' , 14),
#     Cat('Bobby' , 'Tabby' , 'rambunctious' , 0)
# ]