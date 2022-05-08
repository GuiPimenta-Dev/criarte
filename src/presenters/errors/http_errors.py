class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error(status_code: int, error: str):
        """Generic Error"""
        return {"status_code": status_code, "data": {"error": error}}

    @staticmethod
    def error_422():
        """HTTP 422"""
        return {"status_code": 422, "data": {"error": "Unprocessable Entirty"}}

    @staticmethod
    def error_400():
        """HTTP 400"""

        return {"status_code": 400, "data": {"error": "Bad Request"}}

    @staticmethod
    def error_409():
        """HTTP 409"""

        return {"status_code": 409, "data": {"error": "Conflict"}}

    @staticmethod
    def error_500():
        """HTTP 500"""

        return {"status_code": 500, "data": {"error": "Internal Server Error"}}
