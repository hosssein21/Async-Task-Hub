import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task, TaskStatus
from app.schemas.task import TaskCreate


async def create_task(
    session: AsyncSession,
    task_data: TaskCreate,
) -> Task:
    task = Task(
        task_type=task_data.task_type,
        payload=task_data.payload,
        status=TaskStatus.PENDING,
    )

    session.add(task)

    await session.commit()
    await session.refresh(task)

    return task


async def get_task(
    session: AsyncSession,
    task_id: uuid.UUID,
) -> Task | None:
    return await session.get(Task, task_id)