from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)
from CustomConstruct.hitcounter import HitCounter


class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # my_lambda = _lambda.Function(
        #     self, 'HelloNewHandler',
        #     runtime=_lambda.Runtime.PYTHON_3_9,
        #     code=_lambda.Code.from_asset('lambda'),
        #     handler='hello.handler',
        # )
        #
        # hello_with_hitcounter = HitCounter(
        #     self, 'HelloHitCounter',
        #     downstream=my_lambda
        # )
        #
        # apigw.LambdaRestApi(self, "NewEndpoint",
        #                     handler=my_lambda)

