from django.db import models

from access.models import User
from project.models import AbstractModel


class ReportReason(models.TextChoices):
    SPAM = "SPAM", "Spam or Unwanted Content"
    HARASSMENT = "HARASSMENT", "Harassment or Bullying"
    HATE_SPEECH = "HATE", "Hate Speech or Symbols"
    VIOLENCE = "VIOLENCE", "Violence or Dangerous Behavior"
    NUDITY = "NUDITY", "Nudity or Sexual Content"
    MISINFORMATION = "MISINFO", "Misinformation"
    COPYRIGHT = "COPYRIGHT", "Copyright Violation"
    OTHER = "OTHER", "Other"


class AbstractReport(AbstractModel):

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(
        blank=True,
        null=True,
    )
    reason = models.CharField(choices=ReportReason.choices, max_length=12)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


# class CommentReport(AbstractReport):

#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.comment}: {self.reason}"
