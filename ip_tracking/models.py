from django.db import models

class RequestLog(models.Model):
    """Model to store request logs."""
    
    # IP address of the client (supports both IPv4 and IPv6)
    ip_address = models.CharField(max_length=45)
    
    # Timestamp of when the request was made
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # URL path that was requested (e.g., '/login')
    path = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ip_address} accessed {self.path} at {self.timestamp}"
