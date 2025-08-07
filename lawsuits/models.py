from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Lawsuit(models.Model):
    CASE_TYPES = [
        ('criminal', 'قضية جنائية'),
        ('civil', 'قضية مدنية'),
        ('commercial', 'قضية تجارية'),
        ('family', 'قضية أسرية'),
        ('other', 'أخرى'),
    ]

    STATUS_CHOICES = [
        ('received', 'تم الاستلام'),
        ('under_review', 'قيد المراجعة'),
        ('scheduled', 'تم الجدولة'),
        ('assigned', 'تم الإحالة إلى المحامي'),
        ('archived', 'تم الأرشفة'),
    ]

    title = models.CharField(max_length=255, verbose_name='عنوان القضية')
    description = models.TextField(verbose_name='تفاصيل القضية')
    case_type = models.CharField(max_length=20, choices=CASE_TYPES, verbose_name='نوع القضية')
    client_name = models.CharField(max_length=255, verbose_name='اسم العميل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received', verbose_name='الحالة')
    notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    attachment = models.FileField(upload_to='lawsuit_attachments/', blank=True, null=True, verbose_name='مرفقات')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_lawsuits', verbose_name='تم الإحالة إلى')

    def __str__(self):
        return f"{self.title} - {self.client_name}"
