import inspect
import os

from django.core.management import base


class BaseCommand(base.BaseCommand):
    @property
    def command_name(self):
        filename = inspect.getfile(self.__class__)
        return os.path.splitext(os.path.basename(filename))[0]

    def log_message(self, message):
        self.stdout.write(message)

    def log_success(self, message):
        self.stdout.write(self.style.SUCCESS(f"[SUCCESS] {message}"))

    def log_error(self, message):
        self.stdout.write(self.style.ERROR(f"[ERROR] {message}"))

    def log_warning(self, message):
        self.stdout.write(self.style.WARNING(f"[WARNING] {message}"))
