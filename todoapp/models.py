from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eintrag(models.Model):
    content = models.CharField(("Eintrag"), max_length=80)
    done = models.BooleanField(("Erledigt"), default = False)
    created = models.DateTimeField(("Erstellt"), auto_now=False, auto_now_add=True)
    changed = models.DateTimeField(("Verändert"), auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, verbose_name=("Benutzer"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Eintrag")
        verbose_name_plural = ("Einträge")

    def __str__(self):
        erledigt = ""
        if self.done:
            erledigt = "erledigt"
        else:
            erledigt = "offen"
        return f"{self.user} ({str(self.created)}) - {self.content} ({erledigt})"

    #def get_absolute_url(self):
    #    return reverse("entry_detail", kwargs={"pk": self.pk})
