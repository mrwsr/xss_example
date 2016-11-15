from django.utils.deprecation import MiddlewareMixin


class NoXSSProtection(MiddlewareMixin):
    """
    Ensure browser XSS protection is disabled.
    """

    def process_response(self, request, response):
        response['x-xss-protection'] = '0'
        return response
