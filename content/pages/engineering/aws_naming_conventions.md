Title: AWS Naming Conventions 
Date: Tue 14 Sep 2021 00:26:43 AEST
Category: Engineering 
Tags: engineering,terraform,infrastructure,cloud 
Slug: aws_naming_conventions 
Author: Carl Hattingh 
Summary: AWS Naming 
Status: Draft

##  Resource Tagging Policy

**NB:  Tags are case sensitive**

All tags should be in lowercase, with the exception of Name

- Name
- project
- environment
- repo


##  AWS Resource Naming

- Use hyphens/dashes in human readable names
- S3 buckets should always be DNS compliant to facilitate the use of Transfer Acceleration endpoints if needed

The following naming convention formats is suggested:

Naming convention when not including a Region or Availability Zone
```
<project>-<name>-<environment>
```
Naming convention when including a Region where applicable
```
<project>-<name>-<region>-<environment>
```

Naming convention when including an Availability Zone where applicable
```
<project>-<name>-<az-id>-<environment>

```


### Region Codes


Use the region portion of the AZ ID:

E.G: `ap-southeast-2a` could be `apse2-az3`


### Availability Zone ID

Use the AZ ID to designate a specific Availability Zone.


Full Example (an EC2 Instance in a specific AZ)
```
api-nomad-server-apse2-az3-prod
```


### Locating AZ ID's:

- Browse to https://ap-southeast-2.console.aws.amazon.com/ram

- `aws ec2 describe-availability-zones --region <region>`

-  The Terraform "aws_availability_zone"


### S3 Bucket Naming

As buckets are globally unique, it is suggested that bucket names are prepended with the organisation signifier.

```
<org>-<name>-<env>
```

Full example:
```
s3://company-example-bucket-prod

``````
