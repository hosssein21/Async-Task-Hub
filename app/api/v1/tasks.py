import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db_session
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task, get_task


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_task_endpoint(
    task_data: TaskCreate,
    session: AsyncSession = Depends(get_db_session),
) -> TaskResponse:
    task = await create_task(
        session=session,
        task_data=task_data,
    )

    return task


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
async def get_task_endpoint(
    task_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> TaskResponse:
    task = await get_task(
        session=session,
        task_id=task_id,
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task