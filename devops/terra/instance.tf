resource "aws_instance" "dev-inst" {

  ami                    = var.AMI[var.REGION]
  instance_type          = var.INSTANCE_TYPE.t2
  availability_zone      = var.ZONE1
  key_name               = "dev-key"
  vpc_security_group_ids = ["sg-06e0d665c367fd64c"]
  tags = {
    Name    = "dev-instance"
    project = "dev"
  }

}
