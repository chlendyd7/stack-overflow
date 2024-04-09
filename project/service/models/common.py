from django.db import models
import datetime

# Create your models here.
class BaseModel(models.Model):
    
    class Meta:
        abstract = True
    
    created_at=models.DateTimeField(
        verbose_name='생성 일시',
        auto_now_add=True,
    )
    updated_at=models.DateTimeField(
        verbose_name='업데이트 일시',
        auto_now=True,
    )
    removed_at=models.DateTimeField(
        verbose_name='삭제 일시',
        null=True,
        blank=True,
    )

    def delete(self, using=None, keep_parents=False):
        self.removed_at = datetime.datetime.now()
        self.save()

    def force_delete(self):
        super().delete()
