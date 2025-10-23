from django.db import models
from django.contrib.auth.models import User

class FoodPost(models.Model):
    """Model for food posts shared by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_posts')
    food_type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    donor_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Price in Rupees (0.00 for free)")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.food_type} by {self.donor_name}"
    
    def interest_count(self):
        """Return the number of users interested in this post"""
        return self.interests.count()


class Interest(models.Model):
    """Model for users expressing interest in buying/claiming food"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    food_post = models.ForeignKey(FoodPost, on_delete=models.CASCADE, related_name='interests')
    message = models.TextField(blank=True, null=True, help_text="Optional message to the donor")
    contact_info = models.CharField(max_length=200, help_text="Phone or email for contact")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'food_post']  # Prevent duplicate interest from same user
    
    def __str__(self):
        return f"{self.user.username} interested in {self.food_post.food_type}"
