from pydantic import BaseModel

class HealthCheckResponseDTO(BaseModel):
    status: str
    message: str