from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Example Command"

    def add_arguments(self, parser):
        parser.add_argument(
            "--execute",
            action="store_true",
            default=False,
        )

    def handle(self, *args, **kwargs):
        print("Example" if kwargs["execute"] else "Example DRY RUN")
