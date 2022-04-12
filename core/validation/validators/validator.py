from abc import ABC, abstractmethod

from core.dataclasses.model_schema import ModelSchema
from core.dataclasses.request_schema import RequestSchema
from core.validation.responses.validation_response import ValidatorResponse


class Validator(ABC):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        self._model: ModelSchema = model
        self._request: RequestSchema = request

    @abstractmethod
    def validate(self) -> ValidatorResponse:
        pass
