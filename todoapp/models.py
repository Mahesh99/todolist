from django.db import models

class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False) # when a new todo is created it is yet to be done
    
    def __str__(self):
        return f'{self.content}'