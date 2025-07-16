from typing import Any
from django . conf import settings
from ip_tracking . models import RequestLog
from ipware import get_client_ip # type: ignore

class IpLoggingMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request) -> Any:
        client_ip, is_routable = get_client_ip(request)
        if client_ip:
            RequestLog.objects.create(
                ip_adress = client_ip,
                path = request.path
            )
        response = self.get_response(request)
        return response
    