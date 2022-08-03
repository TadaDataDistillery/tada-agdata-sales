variable "env" {
    default =  "sandbox"
}

variable "region" {
    default = "us-east-1"
}

variable "owner_tag" {
    default = "Xerris DevOps Team"
}

variable "SSOPowerUserId" {
    description = "AWS SSO PowerUser IAM ID"
}

variable "SSOAdminUserId" {
    description = "AWS SSO Administrator IAM ID"
}
