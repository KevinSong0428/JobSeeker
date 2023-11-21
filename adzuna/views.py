from django.shortcuts import render
from rest_framework.views import APIView
import requests
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .util import *
from django.conf import settings


class GetJobs(APIView):
    def get(self, request, format=None):
        # list of supported region
        # at, au, be, br, ca, ch, de, es, fr, gb, in, it, mx, nl, nz, pl, sg, us, za"
        region = request.query_params.get("country", "us")
        location = request.query_params.get("location", "New York")
        page = request.query_params.get("page", '1')
        what = request.query_params.get("what", '')
        url = f"https://api.adzuna.com/v1/api/jobs/{region}/search/{page}?app_id=1ad80c2e&app_key=5bf2dd29a2b0e552e157cddca9d7e2cb&what=software engineer&where={location}"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        print(data)
        return Response(data, status=status.HTTP_200_OK)