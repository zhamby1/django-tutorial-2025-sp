from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #remember we can add functions to models
    #sometimes we will want the functions in our views.py file, but usually when we are doing internal database stuff we put it in the models file
    #later on we will publish this post from a draft page...so lets create a publish function that will add and save a publish date

    def publish(self):
        self.published_date = timezone.now()
        #we now need to save it to the DB
        self.save()
    
    #we will create a function that when we are in the python interpreter and call the name Post, it returns the title as a string
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text