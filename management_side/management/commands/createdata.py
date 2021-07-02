from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from management_side.models import *
from random import randint
import random


FLOOR =[
    "1st",
    "2nd",
    "3rd",
    "4th",
    "5th",
    "6th"
]

CATEGORIES =[
    "Action",
    "Adventure",
    "Novel",
    "Detective",
    "Mystery",
    "Fantasy",
    "Historical Fiction",
    "Horror",
    "Literary Fiction",
    "Fantasy",
    "Romance",
    "Contemporary",
    "Dystopian",
    "Mystery",
    "Horror",
    "Thriller",
    "Paranormal",
    "Historical fiction",
    "Science Fiction",
    "Memoir",
    "Cooking",
    "Art",
    "Self-help / Personal",
    "Development",
    "Motivational",
    "Health",
    "History",
    "Travel",
    "Guide / How-to",
    "Families & Relationships",
    "Humor",
    "Children’s"
]


CONDITION =[
    "bad",
    "normal",
    "good"
]
        

STATUS =[
    "pending",
    "delivered",
    "out of date",
    "available"
]


class Provider(faker.providers.BaseProvider):
    def book_category(self):
        return self.random_element(CATEGORIES)
    def book_status(self):
        return self.random_element(STATUS)
    def book_condition(self):
        return self.random_element(CONDITION)
    def book_floor(self):
        return self.random_element(FLOOR)


class Command(BaseCommand):
    help ="Command information"

    def handle(self,*args,**kwargs):
        fake =Faker()
        fake.add_provider(Provider)
        #print(fake.book_category())



        # add Floors
        for _ in range(6):
            Floor.objects.create(floor_id=fake.unique.book_floor())
        


        # add categories
        for _ in CATEGORIES:
            Category.objects.create(cat_name=_,floor_id=random.choice(list(Floor.objects.all())))
        print("success cats adding")



        # add shelves  _ 100shelves in every cat
        for i in Category.objects.all():
            for _ in range(100):
                Shelf.objects.create(cat_id=i)
        print("success shelves adding")



        # create positions  _ all possible positions
        for floor in Floor.objects.all():
            for cat in floor.category_set.all():
                for shelf in cat.shelf_set.all():
                    BookPosition.objects.get_or_create(floor_id=floor,shelf_id=shelf,cat_id=cat)
        print("success pos adding")



        # add books
        seats =BookPosition.objects.all()
        for i in seats:

            Book.objects.create(
                isbn=fake.isbn10(),book_seat=i
                ,title=fake.text(max_nb_chars=30),language=fake.language_name(),
                #bookPhoto="bookPhoto\2021\06\09\lib1.jpg",
                description=fake.paragraph(nb_sentences=2),
                demurage=fake.pyint(),author_name=fake.name(),version_number=randint(1, 5),
                year= fake.date(),condition="good",status="available"
            )
        print("success books adding")