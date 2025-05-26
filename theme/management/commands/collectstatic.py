from django.core.management import call_command
from django.contrib.staticfiles.management.commands.collectstatic import (
    Command as CollectStaticCommand,
)


class Command(CollectStaticCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.NOTICE("📦 Building Tailwind CSS before collectstatic...")
        )
        try:
            call_command("tailwind", "build")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"⚠️ Tailwind build failed: {e}"))
        super().handle(*args, **options)
