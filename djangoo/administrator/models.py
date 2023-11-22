from django.db import models
from blog.models import MyUser
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('d', 'draft')
    )
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    smalldesk = models.CharField(max_length=50)
    desc = models.TextField()
    category = models.ManyToManyField(Category, related_name="post")
    image = models.ImageField(upload_to='image/')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title



class category_Course(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Course(models.Model):
    admin = models.ForeignKey(MyUser, on_delete=models.CASCADE ,related_name="adminUser")
    category = models.ManyToManyField(category_Course, related_name="course")
    title = models.CharField(max_length=50)
    description = models.TextField()
    time = models.CharField(max_length=15)
    timeofcourse = models.CharField(max_length=29)
    image = models.ImageField(upload_to='course/')
    price = models.IntegerField( null=False, blank=False)
    publish = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title



class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='video/')

    def __str__(self):
        return self.title
    
    

class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)



    

    