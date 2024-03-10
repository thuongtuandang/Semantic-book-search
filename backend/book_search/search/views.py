from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from sentence_transformers import SentenceTransformer
from qdrant_client import models, QdrantClient

# Create views here.
class SearchView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = QdrantClient(host='localhost', port=6333)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.results = []

    def search(self, input_text):
        hits = self.client.search(
        collection_name = 'books',
        query_vector = self.model.encode(input_text).tolist(),
        limit = 3
        )
        for idx, hit in enumerate(hits):
            result = {}
            result['index'] = idx+1
            result['isbn13'] = hit.payload['isbn13']
            result['title'] = hit.payload['title']
            result['authors'] = hit.payload['authors']
            result['description'] = hit.payload['description']
            result['average_rating'] = hit.payload['average_rating']
            result['published_year'] = hit.payload['published_year']
            result['thumbnail'] = hit.payload['thumbnail']
            self.results.append(result)

    def post(self, request):
        try:
            data = json.loads(request.body)
            text = data.get("text")
            self.search(text)
            return Response({"results": self.results})
        
        except Exception as e:
            return Response({"error": str(e)}, status=500)