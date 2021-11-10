Title: Source Control Processes 
Date: Tue 07 Sep 2021 20:56:10 AEST
Category: Engineering 
Tags: development,git,PRs,engineering 
Slug: source_control 
Author: Ben Johnston 
Summary: How we use git 

- [Introduction](#introduction)
- [Branching Workflow](#branching-workflow)
- [Commit Messages](#commit-messages)
  - [Anatomy of a Git Commit](#anatomy-of-a-git-commit)
  - [Example Commit Messages](#example-commit-messages)
- [Pull Requests](#pull-requests)
  - [Anatomy of a Pull Request](#anatomy-of-a-pull-request)
    - [Title](#title)
    - [Related Tasks](#related-tasks)
    - [Depends on](#depends-on)
    - [What](#what)
    - [Why](#why)
    - [Concerns](#concerns)
    - [Notes](#notes)
    - [Changes](#changes)
- [Approval Process](#approval-process)
- [Merging](#merging)
- [Versioning, Tagging and Deployment](#versioning-tagging-and-deployment)
- [Hotfixes](#hotfixes)
- [References](#references)

## Introduction

The harrison.ai data engineering team uses [git](https://git-scm.com/) for source control management,
employing a trunk-based development workflow and pull-requests for code review in a style similar
to [the GitHub recommended flow](https://guides.github.com/introduction/flow/).

Key aspects of the workflow include:

* The **`main`** branch is always ready for release or deploy; any code that lands on **`main`** has
  already been reviewed, tested and documented to our high quality standards.
* Releases and deploys are triggered by creating git tags from **`main`**, and are managed by
  our CI/CD infrastructure. Tags follow semantics versioning.
* Work is performed in short-lived feature branches and submitted via pull request, which
  must receive an approving review before being merged to **`main`**. Branch naming conventions
  help us use automated tools to organize our work.

## Branching Workflow 

When working on a development task, the first step is to create an appropriate branch within the correct code repository.  To **ensure the newly created branch is up to date** it is recommended that the branch
be created from the interface of the central repository e.g. github.  If you are creating the branch from a local version of the repo, you must **ensure you fetch the latest updates first**.

The following naming convention is used when creating new branches:

> **`[BRANCH TYPE]/[TASK REFERENCE]-[OPTIONAL DESCRIPTION]`**

where **`[BRANCH TYPE]`** is one of:

* feature
* fix
* chore

and the **`[TASK REFERENCE]`** is the task or ticket number created from Jira.

Examples:

* `feature/PRO-123`
* `fix/FOO-1024-validation-bug`
* `chore/BAR-785-update-barification-docs`

The intent behind this naming convention is that when looking at pull requests or a list of branches for a repository their context can be easily determined by the branch type and more detailed information such as 
the definition of done can be obtained by referring to the corresponding Jira ticket.  This is particularly useful for reviewers of pull requests to ensure the branch meets the requirements of the definition of done.
If setup correctly, Jira will also automatically update the status of the branch within the ticket itself, indicating if a PR (pull request) has been created or even merged. Once you have committed your patch to the branch a pull request is then created, to merge the patch into the original source branch with the name of the branch in the title.

## Commit Messages

Writing clear and meaningful commit messages is a particularly important part of the development process, as they form both a record of the work that has been completed that can be used for later reference, help in communicating with readers or reviewers of your code as well as help to structure the work itself.  By establishing a common commit message format, reading pull requests and commit logs will become a lot easier and more straight forward.  

### Anatomy of a Git Commit

The anatomy of a git commit message used within the data engineering team is as follows:

```markdown
type: Sentence case summary (max 50 chars) #JIRA-123

Detailed summary text, wrapped to 72 characters.  **Ensure**
that the blank line between the Sentence case summary
and this detailed summary text is present.
A bullet point list
 - has a hanging ident

 - with a blank line between lines
```

The key features of the anatomy above are:

* The JIRA (or GitHub) ticket reference.  This is used to ensure the commit is linked to the corresponding ticket and the current status of the task is automatically updated.

* The type of the commit:
    * **feat** for a new feature being added in the commit
    * **fix** for a bug fix
    * **refactor** no changes to the functionality have been made, but some aspect of the codebase has been refactored
    * **test** any commits related to testing
    * **docs** any commits that relate to documentation
    * **chore** regular code maintenance e.g. dependency version bumps
    * **revert** undo a previous commit 

* The sentence case summary, analogous to an email subject line provides the summary of the work done in the commit.  This line is to be no more than 50 characters long and does not end with a fullstop.
* The blank line between the title and the body of the commit message is key for running tools like rebase, however it can be ommitted if the detailed summary text paragraph is not provided.
* (Optional) Detailed summary paragraph(s), each beginning with Capitalisation.  This paragraph is intended to explain the changes made within the commit and why they were made.
* No whitespace errors
* No unnecessary punctuation
* Written using Markdown

In addition to the anatomy of the commit, when writing the message itself you should:

* Use the imperative i.e. use "Fix bug" instead of "Fixed bug" or "Fixed bug"
* Not assume the reader of the commit (or later pull request) has the same knowledge of the original problem being solved, ensure it is described within the message.
* Not consider your code to be self-explanatory, context matters. 
* Use emojis to add some fun 😁🚀

### Example Commit Messages

```markdown
feat: Add dicom to json export JIRA-123

Add `dcm_to_json` method to DicomMgr class to simplify
compatibility with downstream microservices.
```

```markdown
docs: Update installation instructions in README #11 
```

While this seems like a lot to think about for a simple commit message, getting into the habit of writing good commit messages will pay dividends later.

💡 **TIP** Tools such as [commitzen](https://commitizen-tools.github.io/commitizen/) can make creating commit messages a lot easier and in the future this may become a part of our standard toolkit.

## Pull Requests
Just as good commit messages help to communicate the additional context as to how and why changes were made to a codebase, Pull Requests (PRs) also form an important part of this process.  PRs are a key part of developing quality software as they provide a means of:

* ensuring the committed code achieves the desired result
* checking that additional bugs or security vulnerabilities are not introduced to the code base
* assessing the changes for any further increase in maintenance burden
* informing and making other design decisions, as well as
* ensuring the code adheres to agreed upon standards.

Combining the above points with the fact that the code review process involves reviewing what could be many hours hard work of one of your colleagues it is critical that effective communication throughout the review process be maintained.  While direct conversation and pair review should be considered the first and most important step in any PR, the standardised structure and process described within this section of the handbook is to be used to assist in asynchronous work environments and align expectations of the required components within a PR.
The PR process can play a significant role in shaping, informing and reflecting the culture of a team and as such they must be completed with the respect they deserve. 

When done properly a good PR can lead to:

* Higher quality, more efficient and faster code reviews as authors and reviewers of code a like can better understand the problem, context and the code that was written.
* Generating records of design decisions as well as providing input to later project planning stages.
* Better quality code through robust discussion, standardised structure, more readable and testable code.

💡 **TIP** When submitting a patch for a PR keep in mind that one or more of your colleagues will be investing their time to review your work.  The quality of the submitted patch and PR must be respectful of their time and effort.

💡 **TIP** When reviewing a Pull Request remember that you are reviewing the work of your colleague.  The time and effort invested in the review as well as the comments and suggestions must be respectful of the hard work put into the PR.

💡 **TIP** written review comments are unable to communicate tone.  The reader of a comment may misinterpret the meaning intended by the author based on the text alone.  Be considerate of this fact when writing comments or suggestions and if you feel that a particular statement would benefit from further explanation then it may be worth discussing "in-person" before leaving the comment on a PR.

### Anatomy of a Pull Request

Pull Requests and their corresponding descriptions are to adhere to the following format, written using Markdown:

#### Title
The summary of the changes proposed in the PR.  If there is a corresponding ticket number it should be included here.

```markdown
JIRA-123 - Functionality to export DICOM files in JSON format 
```

#### Related Tasks 
For ease of navigation include any tickets that may be related or included in this PR.  It is recommended that this section contain links to the relevant tickets using the method prescribed by the PR system.

```markdown
## Related Tasks
- JIRA-123
- #10 (Github issue link)
```

#### Depends on 
If there are other PRs that need to be reviewed or merged first, or there are other dependencies such as software modules or packages that need to be completed first they should be listed here.
If your PR does not contain any such dependencies, feel free to omit this section.

```markdown
## Depends on
- #15
- [JIRA-789](http://link/to/PR)
```

#### What
What changes have been made within this PR?  In this section describe (not necessarily in technical detail) what changes have been made.  Include in this section any specific design choices that have been made throughout the process e.g. I chose package X over Y because of Z as well as any important background or research that has been completed to justify the changes.  If background work has been completed, include links to the work or informing articles here.  Additionally if there are sections of code that you are not particularly happy with due to other limitations or constraints mention them here with an summary of the limitations and the consequences to the design choices that were made.  Such a description may be useful in informing later tickets or work or may also result in tickets to correct the underlying issue. 

```markdown
## What
I've added a method for exporting DICOM files from the DicomManager
class as a JSON format for use in downstream microservices such as
*magic* as per JIRA-123.  Consistent with other functionality within
the class, the [pydicom](https://pydicom.github.io/pydicom/stable/)
package has been used to execute the JSON conversion as it is the most
mature package for working with DICOM files in Python.  If refer to
line 22 in file `thing.py` you will notice the use of a recursive
function call to assist with DICOM tag conversion as opposed to a
nested for loop.  This was a specific design decision as the DICOM
tags themselves can contain multiple levels of nesting and the
number of levels is variable and unknown.

The API documentation has also been updated to reflect the new feature.
```

#### Why
Why are we submitting this PR?  What is the context, engineering and business goals being satisfied by this PR? 

```markdown
## Why
These changes are required as *magic* and other downstream microservices
require a JSON version of the DICOM file content for sharing contextual
information as a part of the request payload.  This requirement is
defined within JIRA-078 and is being developed within the *magic*
microservice as a part of JIRA-789.  This functionality is being made to
the DicomManager class in this package rather than the downstream packages
to both reduce duplication and ensure a consistent format is shared by all
the downstream microservices.
```

#### Concerns 
This section is optional, however if you have any concerns or questions regarding aspects of the PR, they can be included here.  Including the concerns in this section ensures that they can be discussed as a part of the PR review.

```markdown
## Concerns
The current implementation can include image data in the JSON extract as
is the default within pydicom.  This has the potential to produce JSON
structures which are MB in size and could have negative impacts on calling
microservices.  There currently is no requirement to filter or remove
image data from the JSON extract.
```

#### Notes
This section is also optional and should include anything else that you would like to discuss in the PR review that is not captured elsewhere.

```markdown
## Notes
There are no breaking changes associated with these changes, it is makes
sense to include this feature in the 1.2 release
```

#### Changes
A simple list of changes made to the code.  This often is automatically generated as a part of the PR, including the commits made to complete the work in the pull request.

```markdown
## Changes
feat: Add dicom to json export # JIRA-123
docs: Update API documentation for json export # JIRA-123
```

Putting the entire PR description together:

```markdown
JIRA-123 - Functionality to export DICOM files in JSON format

## Related Tasks
- JIRA-123
- JIRA-789

## Depends on
- [JIRA-789](http://link/to/PR)

## What
I've added a method for exporting DICOM files from the DicomManager
class as a JSON format for use in downstream microservices such as
*magic* as per JIRA-123.  Consistent with other functionality within
the class, the [pydicom](https://pydicom.github.io/pydicom/stable/)
package has been used to execute the JSON conversion as it is the most
mature package for working with DICOM files in Python.  If refer to
line 22 in file `thing.py` you will notice the use of a recursive
function call to assist with DICOM tag conversion as opposed to a
nested for loop.  This was a specific design decision as the DICOM
tags themselves can contain multiple levels of nesting and the
number of levels is variable and unknown.

The API documentation has also been updated to reflect the new feature

## Why
These changes are required as *magic* and other downstream microservices
require a JSON version of the DICOM file content for sharing contextual
information as a part of the request payload.  This requirement is
defined within JIRA-078 and is being developed within the *magic*
microservice as a part of JIRA-789.  This functionality is being made to
the DicomManager class in this package rather than the downstream packages
to both reduce duplication and ensure a consistent format is shared by all
the downstream microservices

## Concerns
The current implementation can include image data in the JSON extract as
is the default within pydicom.  This has the potential to produce JSON
structures which are MB in size and could have negative impacts on calling
microservices.  There currently is no requirement to filter or remove
image data from the JSON extract.

## Notes
There are no breaking changes associated with these changes, it is makes
sense to include this feature in the 1.2 release

## Changes
feat: Add dicom to json export # JIRA-123
docs: Update API documentation for json export # JIRA-123

```
## Approval Process 

In order to merge a branch into **`main`** a pull request must be approved by at least one, preferably two component owners.  These constraints are to be configured at the repository level to ensure a merge cannot be committed without appropriate approval.  The review process, while checking the code satisfies the requirements of the ticket should also ensure that the code adheres to any relevant style guides, as well as the various formatting described within this page.

## Merging 

When a PR has received the necessary approvals, the submitter merges it to
the **`main`** branch.

GitHub's "squash and merge" feature is the preferred merge mechanism, as it 
combines any fixes from review comments into a single commit and automatically
includes a references to the PR number. When multiple commits are being squashed,
take a few moments to edit the final commit message to reflect the "good commit
guidelines" above, and ensure that it contains a refernces to the corresponding
Jira ticket if any.

Merge commits are discouraged, and should only be created when we expect to merge
multiple times from the same branch (such as when merging changes from a public
repository into a private fork).

## Versioning, Tagging and Deployment

To make code available for deployment or consumption by other services,
we make a new git tag from the **`main`** branch. Tags follow the format
and semantics of [Semantic Version 2.0.0](https://semver.org/)
(although the exact details of what constitutes the versioned API surface
may vary between repositories).

Cutting a new tag automatically triggers our CI/CD system to begin a deployment
to production, as appropriate for the repo.

## Hotfixes

We aim to avoid hotfix deployments s much as possible. The preferred way to get
both fixes and features into production is via an ordinary release from latest
**`main`**.

 However, since we may have different consumers running different versions of our
software in their own production environments, it could be necessary to deploy
a hotfix based on some earlier tagged version of the code rather than on latest
**`main`**.

If needed, we create hotfix releases by working on a separate release branch
as follows:

* If one does not already exist, create a new branch named `release-X.Y` based
  an existing `X.Y.Z` release tag.
* Develop the fix as a PR to the `release-X.Y` branch, following the processes
  above.
* Tag a new release `X.Y.(Z+1)` from the `release-X.Y` branch, which will be
  picked up by our CI/CD system to begin a deployment to production.

Trunk-based workflows seem to favour treating these like any other PR - make the
fix, merge it to **`main**`, deploy the new version. This approach seems to favour
projects with frequent deployments to a single target environment, which may not
be a good fit for us.


## References
The following books, articles, blogs were referenced in the creation of this content:

* [https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
* [https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
* [https://maddevs.io/blog/how-to-make-a-proper-description-for-a-pull-request/](https://maddevs.io/blog/how-to-make-a-proper-description-for-a-pull-request/)
* [https://www.pullrequest.com/blog/writing-a-great-pull-request-description/](https://www.pullrequest.com/blog/writing-a-great-pull-request-description/)
* [https://reflectoring.io/meaningful-commit-messages/](https://reflectoring.io/meaningful-commit-messages/)
* [The Git Book](https://git-scm.com/book/en/v2)
