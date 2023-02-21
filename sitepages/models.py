from django.db import models

class PromoName(models.Model):
    """name of the promoted cadet, rank they were promoted to is subclass"""
    name = models.CharField(max_length=70)
    date_added = models.DateTimeField(auto_now_add=True)
    achievment = models.CharField(max_length=150)
    
    def __str__(self):
        """return a string representation of the model"""
        return self.name

class Meeting(models.Model):
    """Future meeting information"""
    meeting_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    week_goal = models.CharField(max_length=150)
    meeting_description = models.TextField()
    
    def __str__(self):
        """return a string representation of the model"""
        return self.week_goal
        
class Event(models.Model):
    """Future event information"""
    event_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    event_title = models.CharField(max_length=150)
    event_description = models.TextField()
    
    def __str__(self):
        """return a string representation of the model"""
        return self.event_title

    
