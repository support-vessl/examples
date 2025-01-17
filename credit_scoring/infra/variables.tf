variable "region" {
  type        = string
  default     = ""
  description = "AWS region where to provision services"
}

variable "project_name" {
  type        = string
  default     = ""
  description = "The project identifier is used to uniquely namespace resources"
}

variable "S3_bucket_name" {
  type = string
  default = "vessl-public-uw2/credit_scoring"
  description = "The S3 bucket name of source data"
}

variable "database_name" {
  type        = string
  default     = "dev"
  description = "The name of the first database to be created when the cluster is created"
}

variable "admin_user" {
  type        = string
  default     = "admin"
  description = "(Required unless a snapshot_identifier is provided) Username for the master DB user"
}

variable "admin_password" {
  type        = string
  default     = ""
  description = "(Required unless a snapshot_identifier is provided) Password for the master DB user"
}

variable "node_type" {
  type        = string
  default     = "dc2.large"
  description = "The node type to be provisioned for the cluster. See https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#working-with-clusters-overview"
}

variable "cluster_type" {
  type        = string
  default     = "single-node"
  description = "The cluster type to use. Either `single-node` or `multi-node`"
}

variable "nodes" {
  type        = number
  default     = 1
  description = "The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node"
}
