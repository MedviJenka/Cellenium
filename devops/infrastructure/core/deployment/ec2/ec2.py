import boto3
from dataclasses import dataclass, field


@dataclass
class CreateEC2Instance:

    """
    Example: CreateEC2Instance(image_id='ami-0f34c5ae932e6f0e4')

    """

    device_name: str = '/dev/xvda'
    region: str = 'us-east-1'
    instance_type: str = 't2.micro'
    image_id: str = ''
    volume_size: int = 8
    security_group: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.client: boto3 = boto3.client('ec2', region_name=self.region)
        self.response = self.client.run_instances(
            BlockDeviceMappings=[
                {
                    'DeviceName': self.device_name,
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': self.volume_size,
                        'VolumeType': 'gp2'
                    },
                },
            ],
            ImageId=self.image_id,
            InstanceType=self.instance_type,
            MaxCount=1,
            MinCount=1,
            Monitoring={
                'Enabled': False
            },
            SecurityGroupIds=self.security_group)
