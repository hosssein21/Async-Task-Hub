import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.task import TaskStatus, TaskType


class TaskCreate(BaseModel):
    task_type: TaskType
    payload: dict


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    task_type: TaskType
    status: TaskStatus
    payload: dict
    result: dict | None
    error: str | None
    created_at: datetime
    started_at: datetime | None
    finished_at: datetime | None