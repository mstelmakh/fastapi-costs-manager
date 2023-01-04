from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from app.models.schemas.operations import (
    Operation,
    OperationCreate,
    OperationUpdate
)
from app.services.operations import OperationsService


router = APIRouter(
    prefix='/operations',
    tags=['operations'],
)


@router.get(
    '/',
    response_model=List[Operation],
)
def get_operations(
    operations_service: OperationsService = Depends(),
):
    return operations_service.get_many()


@router.post(
    '/',
    response_model=Operation,
    status_code=status.HTTP_201_CREATED,
)
def create_operation(
    operation_data: OperationCreate,
    operations_service: OperationsService = Depends(),
):
    return operations_service.create(operation_data)


@router.get(
    '/{operation_id}',
    response_model=Operation,
)
def get_operation(
    operation_id: int,
    operations_service: OperationsService = Depends(),
):
    return operations_service.get(operation_id)


@router.put(
    '/{operation_id}',
    response_model=Operation,
)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    operations_service: OperationsService = Depends(),
):
    return operations_service.update(
        operation_id,
        operation_data
    )


@router.delete(
    '/{operation_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_operation(
    operation_id: int,
    operations_service: OperationsService = Depends(),
):
    operations_service.delete(
        operation_id
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
