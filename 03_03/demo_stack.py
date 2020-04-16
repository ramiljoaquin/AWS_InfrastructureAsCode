from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_autoscaling as autoscaling


class DemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc= ec2.Vpc(self, 'OurDemoVPC',cidr='10.1.0.0/16', max_azs=2,        
                    subnet_configuration=[
                { 'cidrMask': 24, 'name': 'Web', 'subnetType': ec2.SubnetType.PUBLIC},
                { 'cidrMask': 24, 'name': 'Application', 'subnetType': ec2.SubnetType.PRIVATE},
        ])
        
        asg = autoscaling.AutoScalingGroup(
        self,
        "ASG",
        vpc=vpc,
        instance_type=ec2.InstanceType.of(
        ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
        ),
        
        machine_image=ec2.AmazonLinuxImage()
        )

        asg.add_user_data(
        """
        yum update -y
        yum install httpd -y
        echo 'Hello from the CDK' > /var/www/html/index.html
        service httpd start
        chkconfig httpd on
        """
        )

