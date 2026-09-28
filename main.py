import init_django_orm  # noqa: F401

from django.db.models import QuerySet, Model
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    Actor.objects.create(first_name="Jaden", last_name="Smith")

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(first_name="George", last_name="Klooney")
    actor.first_name = "George"
    actor.last_name = "Clooney"
    actor.save()

    actor2 = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor2.first_name = "Keanu"
    actor2.last_name = "Reeves"
    actor2.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")