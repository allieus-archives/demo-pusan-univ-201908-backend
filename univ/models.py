from django.db import models
from django.core.validators import RegexValidator

# blank/null 은 디폴트로 모두 False
class Professor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,
                             validators=[
                                 RegexValidator(r'^010\d{8}$', message='휴대폰 번호를 넣어주세요.')
                             ])
    email = models.EmailField(blank=True)
    department_name = models.CharField(max_length=100, blank=True)
