from django.contrib.auth.models import AbstractUser
from django.db import models

# ✅ أنواع المستخدمين
USER_TYPES = [
    ('client', 'عميل'),
    ('lawyer', 'محامي'),
    ('reception', 'موظف استقبال'),
    ('reviewer', 'مدقق قانوني'),
    ('scheduler', 'موظف جدولة'),
    ('notifier', 'مسؤول تواصل'),
    ('admin', 'مدير النظام'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='client')
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"
