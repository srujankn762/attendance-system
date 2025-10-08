import json
import logging
import threading
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("django.request")


class LogRequestResponseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        thread = threading.current_thread()
        try:
            body = request.body.decode("utf-8")
        except Exception:
            body = "<non-decodable body>"

        logger.info(
            f"[REQUEST] {request.method} {request.get_full_path()} "
            f"Thread: {thread.name} ({thread.ident}) | "
            f"Headers: {dict(request.headers)} | "
            f"Body: {body}"
        )
        return None

    def process_response(self, request, response):
        thread = threading.current_thread()
        try:
            if hasattr(response, "content"):
                content = response.content.decode("utf-8")[:2000]  # limit size
            else:
                content = "<no content>"
        except Exception:
            content = "<non-decodable content>"

        logger.info(
            f"[RESPONSE] {request.method} {request.get_full_path()} "
            f"Status: {response.status_code} "
            f"Thread: {thread.name} ({thread.ident}) | "
            f"Response: {content}"
        )
        return response
