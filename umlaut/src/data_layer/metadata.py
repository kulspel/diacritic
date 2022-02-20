# NOTE not sure if this belongs here, should probably be in some model package
from typing import TypedDict


class IdServiceMetadata(TypedDict):
    id_counter: int


class Metadata(TypedDict):
    id_service: IdServiceMetadata
