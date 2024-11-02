import pathlib
import uuid

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Annotated

from starlette.responses import JSONResponse

from db.interfaces.PhotoInterface import PhotoInterface
from db.minioTool import minioApi
from db.models import Task, User, Photo  # Обязательно укажите правильный путь к вашей модели Task
from db.interfaces.DatabaseInterface import \
    DatabaseInterface  # Убедитесь, что импортируете правильный интерфейс базы данных
from db.database import get_db_session  # Импортируйте свою зависимость для получения сессии базы данных
from models.models import TaskCreate, TaskUpdate, Task as pdTask, Message, PdPhoto, EmployeeCreate, EmployeeGet
from security.security import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)



@router.post("/",
             summary="Create a new employee record",
             description="Creates a new employee record in the database. "
                         "Requires fields such as name, surname, position, department, phone, email, and is_active status. "
                         "This endpoint checks for an existing employee with the same email before creating a new record.",
             responses={
                 401: {"model": Message, "description": "Could not validate credentials"},
                 200: {"description": "Employee created", "model": Message},
                 404: {"description": "No tasks found"}
             },
             )
async def create_employee(task: EmployeeCreate,
                          user: Annotated[User, Depends(get_current_user)],
                          db: Annotated[AsyncSession, Depends(get_db_session)]):
    pass  # TODO Implement this


@router.get("/", response_model=List[EmployeeGet],
            responses={
                401: {"model": Message, "description": "Could not validate credentials"},
                200: {"description": "A list of employees", "model": List[EmployeeGet]},
                404: {"description": "No employees found"}
            },
            summary="Retrieve a list of employees",
            description="Fetches a list of employees from the database. "
                        "The result can be paginated using the skip and limit query parameters."
            )
async def read_employees(user: Annotated[User, Depends(get_current_user)],
                     skip: int = 0,
                     limit: int = 10,
                     db: AsyncSession = Depends(get_db_session)):
    pass  # TODO Implement this

@router.get("/{employee_id}", response_model=EmployeeGet,
            summary="Retrieve a specific task",
            description="Fetches a specific employee by its ID. "
                        "This endpoint requires authentication, and the user must be logged in.",
            responses={
                200: {"description": "Employee found", "model": EmployeeGet},
                401: {"model": Message, "description": "Could not validate credentials"},
                404: {"description": "Employee not found"}
            }
            )
async def read_task(employee_id: int,
                    user: Annotated[User, Depends(get_current_user)],
                    db: AsyncSession = Depends(get_db_session)):
    pass  # TODO Implement this


@router.put("/{employee_id}", response_model=EmployeeCreate,
            summary="Update a specific employee",
            description="Updates the details of a specific employee identified by its ID. "
                        "Only the fields provided in the request body will be updated.",
            responses={
                200: {"description": "Employee updated successfully", "model": Message},
                404: {"description": "Employee not found"},
                401: {"model": Message, "description": "Could not validate credentials"},
                400: {"description": "Invalid input data"}
            }
            )
async def update_task(employee_id: int,
                      user: Annotated[User, Depends(get_current_user)],
                      employee_update: EmployeeCreate, db: AsyncSession = Depends(get_db_session)):
    pass  # TODO Implement this


@router.delete("/{employee_id}", response_model=Message,
               summary="Delete a specific employee",
               description="Deletes a employee identified by its ID. "
                           "Returns a confirmation message upon successful deletion.",
               responses={
                   200: {"description": "employee deleted successfully"},
                   404: {"description": "employee not found"},
                   401: {"model": Message, "description": "Could not validate credentials"},
               }
               )
async def delete_task(employee_id: int,
                      user: Annotated[User, Depends(get_current_user)],
                      db: AsyncSession = Depends(get_db_session)):
    pass  # TODO Implement this

@router.post("/{employee_id}/photos/", response_model=Message,
             summary="Upload a photo for a specific employee",
             description="Uploads a photo for a employee identified by its ID. "
                         "Returns a confirmation message upon successful upload.",
             responses={
                 200: {"description": "Photo uploaded successfully"},
                 404: {"description": "Employee not found"},
                 422: {"description": "Invalid file format or upload issue"},
                 401: {"model": Message, "description": "Could not validate credentials"},
             }
             )
async def upload_photo(employee_id: int,
                       user: Annotated[User, Depends(get_current_user)],
                       db: Annotated[AsyncSession, Depends(get_db_session)],
                       file: UploadFile = File(...)):
    pass  # TODO Implement this


@router.get("/{employee_id}/photos/", response_model=List[PdPhoto],
            summary="Retrieve photos associated with a employee",
            description="Fetches a list of photos related to a specific employee identified by its ID.",
            responses={
                200: {
                    "description": "A list of photos associated with the employee.",
                    "content": {
                        "application/json": {
                            "example": [
                                {
                                    "id": 1,
                                    "url": "http://example.com/photo1.png"
                                },
                                {
                                    "id": 2,
                                    "url": "http://example.com/photo2.png"
                                }
                            ]
                        }
                    },
                },
                404: {"description": "employee not found"},
                401: {"model": Message, "description": "Could not validate credentials"},
            }
            )
async def get_task_photos(task_id: int,
                          user: Annotated[User, Depends(get_current_user)],
                          db: Annotated[AsyncSession, Depends(get_db_session)]):
    pass  # TODO Implement this
