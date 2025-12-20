from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(tags=["Images"])


@router.get("/images")
def list_images(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Paginated list of images
    """
    offset = (page - 1) * limit

    total = db.query(models.Image).count()

    images = (
        db.query(models.Image)
        .order_by(models.Image.id.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "data": images,
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": (total + limit - 1) // limit,
    }






















#  from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from typing import List
# from ..database import get_db
# from .. import models, schemas

# router = APIRouter(tags=["Images"])

# @router.get("/images", response_model=List[schemas.ImageOut])
# def list_images(db: Session = Depends(get_db)):
#     images = db.query(models.Image).order_by(models.Image.id.desc()).all()
#     return images
