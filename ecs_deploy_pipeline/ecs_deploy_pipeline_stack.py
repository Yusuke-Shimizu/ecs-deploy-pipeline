from aws_cdk import (
    aws_ec2 as ec2, 
    aws_ecs as ecs, 
    aws_ecs_patterns as ecs_patterns,
    core
)

class EcsDeployPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # import default VPC
        vpc = ec2.Vpc.from_lookup(self, 'VPC', is_default=True)

        # ECS cluster
        cluster = ecs.Cluster(self, 'Cluster', vpc=vpc)

        task = ecs.FargateTaskDefinition(self, 'Task',
                                             cpu=256,
                                             memory_limit_mib=512,
        #                                      )
        # task.add_container('flask',
        #                   image=ecs.ContainerImage.from_asset('flask-docker-app'),
        #                   environment={
        #                       'PLATFORM': 'AWS Fargate :-)'
        #                   }
        #                   ).add_port_mappings(ecs.PortMapping(container_port=5000))

        # svc = ecs_patterns.ApplicationLoadBalancedFargateService(self, 'svc',
        #                                                              cluster=cluster,
        #                                                              task_definition=task
        #                                                              )

        # core.CfnOutput(self, 'SericeURL', value="http://{}".format(
        #     svc.load_balancer.load_balancer_dns_name))
