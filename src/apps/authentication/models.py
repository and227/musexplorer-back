from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(AbstractUser):
    pass
    # username = models.CharField(blank=True, null=True)
    # email = models.EmailField(_('email address'))