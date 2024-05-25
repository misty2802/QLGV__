from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.exceptions import ValidationError

class Department(models.Model):
    departmentID = models.CharField(max_length=7, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.departmentID and not Department.objects.filter(name=self.name).exists(): 
            self.departmentID = self.generate_departmentID()
        else:
        # Xử lý trường hợp tên bộ phận trùng lặp ở đây, có thể ghi log hoặc thực hiện hành động phù hợp
            raise ValidationError("Tên bộ phận đã tồn tại trong cơ sở dữ liệu.")
        super().save(*args, **kwargs)

    @staticmethod
    def generate_departmentID():
        prefix = "DE"
        count = Department.objects.count()
        if count == 0:
            return f"{prefix}00001"
        next_id = f"{prefix}{count+1:05}"
        while Department.objects.filter(departmentID=next_id).exists():
            count += 1
            next_id = f"{prefix}{count+1:05}"
        return next_id

    def __str__(self):
        return self.name
    
class Instructor(models.Model):
    instructorID = models.CharField(max_length=7, primary_key=True, editable=False)
    image =models.ImageField(upload_to='images/instructorAvatars/') 
    name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    POSITION_CHOICES = [
        ('Trợ giảng', "Trợ giảng"),
        ('Giảng viên', "Giảng viên"),
        ('Phó giáo sư', "Phó giáo sư"),
        ('Giáo sư', "Giáo sư"),
    ]
    EDUCATIONLEVEL_CHOICES = [
        ('Cử nhân', "Cử nhân"),
        ('Thạc sĩ', "Thạc sĩ"),
        ('Tiến sĩ', "Tiến sĩ"),
    ]
    
    STATUS_CHOICES = [
        ('Đang dạy', "Đang dạy"),
        ('Nghỉ hưu', "Nghỉ hưu"),
        ('Nghỉ việc', "Nghỉ việc"),
        ('Hợp đồng', "Hợp đồng"),
        ('Nghỉ phép', "Nghỉ phép"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey('Department', to_field='departmentID', on_delete=models.CASCADE)
    place_of_birth = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100, choices=EDUCATIONLEVEL_CHOICES)
    job_position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    status = models.CharField(max_length=50,choices= STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.instructorID:
            self.instructorID = self.generate_instructorID()
        super().save(*args, **kwargs)
    @staticmethod
    def generate_instructorID():
        prefix = "GV"
        count = Instructor.objects.count()
        if count == 0:
            return f"{prefix}00001"
        next_id = f"{prefix}{count+1:05}"
        while Instructor.objects.filter(instructorID=next_id).exists():
            count += 1
            next_id = f"{prefix}{count+1:05}"
        return next_id

    def __str__(self):
        return self.name
@receiver(post_save, sender=Instructor)
def create_user_for_instructor(sender, instance, created, **kwargs):
    """
    Tạo một người dùng mới cho mỗi Instructor được tạo.
    """
    if created:
        # Tạo một user mới
        user = User.objects.create_user(username=instance.instructorID, password='1111', is_staff=False)
# bài báo
class Article(models.Model):
    articleID = models.CharField(max_length=7, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/articleImg/', blank=True, null=True)
    content = models.TextField()
    publish_date = models.DateField(auto_now=True)
    
    upload_file = models.FileField(upload_to='files/', blank=True, null=True)  
    def save(self, *args, **kwargs):
        if not self.articleID:
            self.articleID = self.generate_articleID()
        super().save(*args, **kwargs)
    @staticmethod
    def generate_articleID():
        prefix = "AR"
        count = Article.objects.count()
        if count == 0:
            return f"{prefix}00001"

        next_id = f"{prefix}{count+1:05}"
        while Article.objects.filter(articleID=next_id).exists():
            count += 1
            next_id = f"{prefix}{count+1:05}"
        return next_id
    def __str__(self):
        return self.title