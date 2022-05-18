from abc import ABC, abstractmethod
from typing import Dict


class GetDaysInterface(ABC):
    """Abstract method for get days use case"""

    @abstractmethod
    def get_days(self) -> Dict[str, Dict[str, int]]:
        raise Exception("Should implement method get_days")
