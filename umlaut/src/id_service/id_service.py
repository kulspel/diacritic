from abc import ABC, abstractmethod

Id = int


class IdService(ABC):

    @abstractmethod
    def getId(self): Id
    # NOTE what is the needed input?
    # NOTE this is probably a super ugly hacky solution, and probably should be solved by some other lib/in some other way
