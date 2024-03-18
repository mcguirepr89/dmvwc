from django.db import models

class Caliber(models.Model):
    AUTOMATIC = 'Automatic'
    MECHANICAL = 'Mechanical'
    QUARTZ = 'Quartz'
    OTHER = 'Other'

    TYPE_CHOICES = [
        (AUTOMATIC, 'Automatic'),
        (MECHANICAL, 'Mechanical'),
        (QUARTZ, 'Quartz'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    inhouse = models.BooleanField(null=True, blank=True)

    def __str__(self):
        if self.inhouse == True:
            return f"{self.name} ({self.type}) - In-House"
        else:
            return f"{self.name} ({self.type})"

    @property
    def slug_url(self):
        # Generate and return the full URL using the stored slug
        return f"https://calibercorner.com/{self.slug}"

    class Meta:
        ordering = ['name']
