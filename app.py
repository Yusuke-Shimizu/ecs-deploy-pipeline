#!/usr/bin/env python3

import os
from aws_cdk import core

from ecs_deploy_pipeline.ecs_deploy_pipeline_stack import EcsDeployPipelineStack

app = core.App()

aws_env = {
    'account': os.environ['CDK_DEFAULT_ACCOUNT'],
    'region': os.environ['CDK_DEFAULT_REGION']
    }

EcsDeployPipelineStack(app, "ecs-deploy-pipeline", env=aws_env)

app.synth()
