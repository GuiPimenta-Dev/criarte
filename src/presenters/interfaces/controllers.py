from abc import ABC, abstractmethod
from typing import Dict


class ControllersInterface(ABC):
    """Interface to COntrollers"""

    @abstractmethod
    def handle(self, http_request: Dict):
        """Method to handle request"""
        raise Exception("Should implement handler method")
