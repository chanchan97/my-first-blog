from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #this line defines our model
      author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #this is link to another model
      title = models.CharField(max_length=200) #this is how to define text with a limited number of characters
      text = models.TextField() #this is for long text without a limit. Sounds ideal for blog post content, right ?
      created_date = models.DateTimeField(default=timezone.now)
      published_date = models.DateTimeField(blank=True, null=True)
     
      def publish(self):
          self.published_date = timezone.now()
          self.save
    
      def __str__(self):
          return self.title
