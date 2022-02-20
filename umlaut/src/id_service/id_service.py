from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

# TODO This one needs to be abstracted to it's own package separate from the scraper, since it will be needed in several places


Id = int


@dataclass(frozen=True)
class IdService(ABC):

    @abstractmethod
    def getId(self, obj: Any) -> Id:
        raise NotImplementedError
        # NOTE what is the needed input?
        # NOTE this is probably a super ugly hacky solution, and probably should be solved by some other lib/in some other way
