# -*- coding: utf-8 -*-
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from tools.schemas.annotation_auto_schema import AnnotationAutoSchema


@swagger_auto_schema(methods=["get"], auto_schema=AnnotationAutoSchema)
@api_view(["GET"])
def get_demo_api(request: Request):
    """
    Get方法demo API

    param: input: input参数, string, query, required

    return: 接口返回
    {
        "msg": "返回信息(string)"
    }
    """
    input_param = request.query_params.get("input")
    return Response({"msg": f"这是一个demo接口, 输入参数为: {input_param}"})


@swagger_auto_schema(methods=["post"], auto_schema=AnnotationAutoSchema)
@api_view(["POST"])
def post_demo_api(request: Request):
    """
    Post方法demo API

    body: data
    {
        "input(required)": "上传数据input参数(string)"
    }

    return: 接口返回
    {
        "msg": "返回信息(string)"
    }
    """
    input_param = request.data.get("input")
    return Response({"msg": f"这是一个demo接口, 输入参数为: {input_param}"})
