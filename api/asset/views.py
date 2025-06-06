import uuid
import boto3

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from api.permissions import IsAuthenticated


class InitUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content_type = request.data.get("content_type")
        extension = request.data.get("extension", "jpg")
        filename = request.data.get("filename", None)
        upload_to = request.data.get("upload_to", None)

        if not content_type or not extension:
            return Response({"error": "Missing content type or extension"}, status=400)

        if not filename:
            filename = f"{uuid.uuid4()}.{extension}"

        key = f"{upload_to.rstrip('/') if upload_to else 'uploads'}/{uuid.uuid4()}/{filename}"

        s3 = boto3.client("s3")
        upload_url = s3.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                "Key": key,
                "ContentType": content_type,
                "ACL": "public-read",
            },
            ExpiresIn=300,
            HttpMethod="PUT",
        )

        public_url = (
            f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{key}"
        )

        return Response(
            {"upload_url": upload_url, "public_url": public_url, "key": key}
        )
