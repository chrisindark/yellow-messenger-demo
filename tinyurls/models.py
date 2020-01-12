import binascii
import os

from django.db import models

from core.models import TimestampedModel


# Create your models here.
class TinyUrl(TimestampedModel):
    tiny_id = models.CharField(max_length=10, db_index=True)
    original_url = models.URLField()
    expires_on = models.DateTimeField(null=True, blank=True)
    last_used_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.tiny_id)

    def generate_key(self):
        return binascii.hexlify(os.urandom(5)).decode()
