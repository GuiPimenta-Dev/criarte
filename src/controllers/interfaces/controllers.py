from abc import ABC, abstractmethod
from typing import Any, Dict


class ControllersInterface(ABC):
    """Interface to COntrollers"""

    @abstractmethod
    def handle(self, http_request: Dict) -> Any:
        """Method to handle request"""
        raise Exception("Should implement handler method")
