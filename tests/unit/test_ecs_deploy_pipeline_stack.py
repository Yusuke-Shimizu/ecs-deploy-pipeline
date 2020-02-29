import json
import pytest

from aws_cdk import core
from ecs_deploy_pipeline.ecs_deploy_pipeline_stack import EcsDeployPipelineStack


def get_template():
    app = core.App()
    EcsDeployPipelineStack(app, "ecs-deploy-pipeline")
    return json.dumps(app.synth().get_stack("ecs-deploy-pipeline").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
