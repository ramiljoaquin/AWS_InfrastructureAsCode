from aws_cdk import core
from aws_cdk import aws_ec2 as ec2


class DemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc= ec2.Vpc(self, 'OurDemoVPC',cidr='10.1.0.0/16', max_azs=2,        
                    subnet_configuration=[
                { 'cidrMask': 24, 'name': 'Web', 'subnetType': ec2.SubnetType.PUBLIC},
                { 'cidrMask': 24, 'name': 'Application', 'subnetType': ec2.SubnetType.PRIVATE},
        ])
