from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users_list = [
            {'email': 'user1@hell.ok', 'first_name': 'user1', 'password': '5678'},
            {'email': 'user2@hell.ok', 'first_name': 'user2', 'password': '1234'}
        ]
        user_to_create = []
        for user_item in users_list:
            user_to_create.append(User(**user_item))

            User.objects.bulk_create(user_to_create)
