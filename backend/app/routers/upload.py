from fastapi import APIRouter, UploadFile, File, HTTPException
import cloudinary.uploader
import cloudinary.exceptions

router = APIRouter(prefix="/upload", tags=["Upload"])
@router.post("/gambar")
async def upload_image(file: UploadFile = File(...)):
    try:
        result = cloudinary.uploader.upload(
            file.file,
            folder="si-tpa",
            resource_type="image"
        )

        return {
            "url": result["secure_url"],
            "public_id": result["public_id"]
        }

    except cloudinary.exceptions.Error as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Gagal upload gambar: {str(e)}"
        )
