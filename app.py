#!/usr/bin/env python3

from aws_cdk import core

from ecs_deploy_pipeline.ecs_deploy_pipeline_stack import EcsDeployPipelineStack


app = core.App()
EcsDeployPipelineStack(app, "ecs-deploy-pipeline", env={'region': 'us-west-2'})

app.synth()
