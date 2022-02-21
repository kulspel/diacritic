from abc import ABC, abstractmethod
from dataclasses import dataclass

# TODO This one needs to be abstracted to it's own package separate from the scraper, since it will be needed in several places
# NOTE Will it though?


Id = int


@dataclass(frozen=True)
class IdService(ABC):

    @abstractmethod
    def get_id(self, class_identifier: str) -> Id:
        raise NotImplementedError
        # NOTE what is the needed input?
        # NOTE this is probably a super ugly hacky solution, and probably should be solved by some other lib/in some other way
