from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.
class DateStampedModel(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class IconChoices(models.TextChoices):
    LIGHTBULB = 'bi bi-lightbulb', 'Lightbulb'
    GEAR = 'bi bi-gear', 'Gear'
    ROBOT = 'bi bi-robot', 'Robot'
    CODE = 'bi bi-code-slash', 'Code'
    LINK = 'bi-link', 'Link'
    SEARCH = 'bi bi-search', 'Search'
    BAR_CHART = 'bi bi-bar-chart', 'Bar Chart'
    PIE_CHART = 'bi bi-pie-chart', 'Pie Chart'


class PersonalInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/', default='hero-bg.jpg')
    bio = models.TextField(null=True, blank=True)
    summary = models.TextField()
    position_title = models.CharField(max_length=64)
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Experience(DateStampedModel):
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=100)
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} at {self.company}'

    class Meta:
        ordering = ('-start_date',)


class Education(DateStampedModel):
    institution_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    grade = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.institution_name}, {self.degree} of {self.field_of_study}'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    overview = models.TextField(max_length=500)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/')
    tools = models.TextField()
    category = models.TextField(max_length=100)
    demo = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='certificates/')
    date = models.DateField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=30, choices=IconChoices, default=IconChoices.LIGHTBULB)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Project)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
