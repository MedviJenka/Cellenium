variable "REGION" {
  default = "us-east-1"
}

variable "ZONE1" {
  default = "us-east-1a"
}

variable "AMI" {
  type = map(string)
  default = {
    us-east-1 = "ami-06ca3ca175f37dd66"
  }
}

variable "INSTANCE_TYPE" {
  type = map(string)
  default = {
    t2 = "t2.micro"
  }
}
