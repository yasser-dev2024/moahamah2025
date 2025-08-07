from django.db import models
from django.conf import settings

CASE_TYPES = [
    ('جنائي', 'جنائي'),
    ('مدني', 'مدني'),
    ('أحوال شخصية', 'أحوال شخصية'),
    ('تجاري', 'تجاري'),
    ('عمالي', 'عمالي'),
]

class Case(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    case_type = models.CharField(max_length=50, choices=CASE_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='cases/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
