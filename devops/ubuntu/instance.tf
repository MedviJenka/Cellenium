provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ubuntu_instance" {
  ami               = "ami-053b0d53c279acc90"
  instance_type     = "t2.micro"
  availability_zone = "us-east-1b"
  tags = {
    "Name" = "ubuntu_instance"
  }
}
