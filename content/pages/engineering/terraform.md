Title: Terraform Style Guide 
Date: Tue 14 Sep 2021 00:26:43 AEST
Category: Engineering 
Tags: engineering,terraform,infrastructure 
Slug: terraform 
Author: Carl Hattingh 
Summary: Terraform Style Guide 
Status: Draft

[AWS Naming Conventions]({filename}aws_naming_conventions.html)

##  General

- Use environments in discrete folders, not workspaces, to separate environments
  - Use symlinks wherever possible to avoid repetition.
- Repos should use the 3 Musketeers Pattern, https://3musketeers.io/docs/patterns.html
- Backend:
  - S3 with optional DynamoDB locking
  - Stored in same account as deployed infrastructure
  - Terraform State key naming convention: `<repo>/<stage>/<environment>/tfstate`


### Terraform Syle Guide


### Resource and data source arguments ###

Do not repeat resource type in resource (not partially, nor completely):


**Good:**

```
resource "aws_route_table" "public" {}
```
**Bad:**

```
resource "aws_route_table" "public_route_table" {}
```
**Bad:**
```
resource "aws_route_table" "public_aws_route_table" {}
```

1. Resources name should be named **this** if there is no more descriptive and general name available, or if resource module creates a 
single resource of this type (e.g, there is a single resource of type **aws_nat_gateway** and multiple resources of type **aws_route_table**, 
so **aws_nat_gateway** should be named this and **aws_route_table** should have more descriptive names - like **private**, **public**, **database**).

2. Always use singular nouns for names.

3. Use - inside argument values and in places where the value will be exposed to a human (e.g inside the DNS name of an RDS instance).

4. Include the count argument inside resource blocks as the first argument at the top and separate it by a newline after it.


**Good:**
```
resource "aws_route_table" "public" {
  count = 2

  vpc_id = "vpc-12345678"
  # ... remaining arguments omitted
}

**Bad:**


resource "aws_route_table" "public" {
  vpc_id = "vpc-12345678"
  count = 2

  # ... remaining arguments omitted
}
```
Include the **tags** argument, if supported by the resource as the last real argument, followed by **depends_on** and **lifecycle**, if necessary. 
All of these should be separated by a single empty line.

**Good:**
```
resource "aws_nat_gateway" "this" {
  count         = 1

  allocation_id = "..."
  subnet_id     = "..."

  tags = {
    Name = "..."
  }

  depends_on = [aws_internet_gateway.this]

  lifecycle {
    create_before_destroy = true
  }
}
```

**Bad:**

```
resource "aws_nat_gateway" "this" {
  count = 1

  tags = "..."

  depends_on = [aws_internet_gateway.this]

  lifecycle {
    create_before_destroy = true
  }

  allocation_id = "..."
  subnet_id     = "..."
}

```

When using conditions in the **count** argument use a boolean value, if it makes sense, otherwise use **length** or another interpolation.

```
  count = length(var.public_subnets) > 0 ? 1 : 0
  count = var.create_vpc ? 1 : 0
```
## Variables ##
1. Don't reinvent the wheel in resource modules - use the same variable names, description and default as defined in "Argument Reference" 
   section for the resource you are working on.

2. Omit **type = "list"** declaration if there is **default = []** also.

3. Omit **type = "map"** declaration if there is **default = {}** also.

4. Use the plural form in name of variables of type **list** and **map**.

5. When defining variables order the keys: **description**, **type**, **default**.

6. Always include a description for all variables even if you think it is obvious.

## Outputs ##

Names for outputs are important to make them consistent and understandable outside of its scope (when
a user is using a module it should be obvious what type and the attribute of the value that is returned).

1. The general recommendation for the names of outputs is that it should be descriptive for the value it 
   contains and be less free-form than you would normally want.

2. A good structure for names of output looks like **{name}_{attribute}**, where:
   **{name}** is a resource or data source name without provider prefix. **{name}** for **aws_subnet** is **subnet**,  
   for **aws_vpc** it is **vpc** and **{attribute}** is the attribute returned by the output

3. If the output is returning a value with interpolation functions and multiple resources, the **{name}** and **{attribute}** there should be as generic as possible
   (this is often the most generic and should be preferred).

4. If the returned value is a list it should have a plural name.

5. Always include a description for all outputs even if you think it is obvious.





## Git Repo directory structure:

(incomplete)
(see also cookiecutter)

```
.
├── .env
├── .gitignore
├── Makefile
├── docker-compose.yml
├── envvars.yml
└── tf
    ├── modules
    │   └── module-one
    │       ├── main.tf
    │       ├── outputs.tf
    │       └── variables.tf
    ├── stage-one
    │   ├── dev
    │   └── prod
    └── stage-two
        ├── dev
        └── prod
```
