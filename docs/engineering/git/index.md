# Source Control Processes

- [Source Control Processes](#source-control-processes)
  - [Introduction](#introduction)
  - [Branching Workflow](#branching-workflow)
  - [Commit Messages](#commit-messages)
  - [Pull Requests](#pull-requests)
  - [References](#references)

## Introduction

The harrison.ai data engineering team uses [git](https://git-scm.com/) for source control management and employs the git flow workflow; if you are not familiar or need a refresher on git flow, this explanation by Atlassian [https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) is a useful reference.

![](branches.svg)
Source: [Atlassian gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

Almost all of our git repositories consist of the following branch types:
* **main**: is the production release branch that contains the code operating within the production environment.  With the exception of **hotfixes**, code can only reach the **main** branch following a pull request and by merging in from the **develop** or in some circumstances a **release** branch.
* **develop**: is the deployment branch for the development environment.  The develop branch is used as a means of testing patches and features intended for release into the **main** branch.
* **feature**: a branch created from **develop** that is used to develop and add new features to the code base.
* **bugfix**: a branch created from **develop** that is used to implement fixes to reported issues. 
* **hotfix**: hotfix branches created from the **master** branch are used for fixes that must be quickly applied to production code.  Once these branches are merged into master, a merge from **master** into **develop** is also required.

Currently the data engineering team does not employ a dedicated **release** branch, due to the size of the team working on the code base and the desire for fast feedback cycles with production. 

## Branching Workflow 

When working on a development task, the first step is to create an appropriate branch within the correct code repository.  To ensure **the newly created branch is up to date** it is recommended that the branch
be created from the interface of the central repository e.e. github.  If you are creating the branch from a local version of the repo, you must **ensure you fetch the latest updates first**.  Whichever method is used, ensure you
are branching from **develop** with the exception of **hotfix** braanches which are created from **main**.

The following naming convention is to be used when creating new branches:

> **BRANCH TYPE/TASK REFERENCE**

where **BRANCH TYPE** is one of:

* feature
* bugfix
* hotfix

and the **TASK REFERENCE** is the task or ticket number created from Jira.

Examples:

> feature/PRO-123
>
> bugfix/FOO-1024
>
> hotfix/BAR-785

The intent behind this naming convention is that when looking at pull requests or a list of branches for a repository their context can be easily determined by the branch type and more detailed information such as 
the definition of done can be obtained by referring to the corresponding Jira ticket.  This is particularly useful for reviewers of pull requests to ensure the branch meets the requirements of the definition of done.
If setup correctly, Jira will also automatically update the status of the branch within the ticket itself, indicating if a PR (pull request) has been created or even merged.Once you have committed your patch to the branch a pull request is then created, to merge the patch into the original source branch with the name of the branch in the title.


## Commit Messages

Writing clear and meaningful commit messages are a particularly important part of the development process, as they form both a record of the work that has been completed that can be used for later reference, help in communicating with readers or reviewers of your code as well as help to structure the work itself.  By establishing a common commit message format, reading pull requests and commit logs will become a lot easier and more straight forward.  
The anatomy of a git commit message used within the data engineering team is as follows:

> type: Sentence case summary (max 50 chars) #JIRA-123
>
> Detailed summary text, wrapped to 72 characters.  **Ensure**
> that the blank line between the Sentence case summary
> and this detailed summary text is present.
> A bullet point list
>  - has a hanging ident
>
>  - with a blank line between lines

The key features of the anatomy above are:
* The JIRA (or Github) ticket reference.  This is used to ensure the commit is linked to the corresponding ticket and the current status of the task is automatically updated.
* The type of the commit:
  * **feat** for a new feature being added in the commit
  * **fix** for a bug fix
  * **refactor** no changes to the functionality have been made, but some aspect of the codebase has been refactored
  * **test** any commits related to testing
  * **docs** any commits that relate to documentation
  * **chore** regular code maintenance e.g. dependency version bumps
* The sentence case summary, analogous to an email subject line provides the summary of the work done in the commit.  This line is to be no more than 50 characters long and does not end with a fullstop.
* The blank line between the title and the body of the commit message is key for running tools like rebase, however it can be ommitted if the detailed summary text paragraph is not provided.
* (Optional) Detailed summary paragraph(s), each beginning with Capitalisation.  This paragraph is intended to explain the changes made within the commit and why they were made.
* No whitespace errors
* No unnecessary punctuation

In addition to the anatomy of the commit, when writing the message itself you should:
* Use the imperative i.e. use "Fix bug" instead of "Fixed bug" or "Fixed bug"
* Not assume the reader of the commit (or later pull request) has the same knowledge of the original problem being solved, ensure it is described within the message.
* Not consider your code to be self-explanatory, context matters. 
* Use emojis to add some fun 😁🚀

**Example Commit Messages**

```
JIRA-123 # feat: Add dicom to json export

Add `dcm_to_json` method to DicomMgr class to simplify
compatibility with downstream microservices.
```

```
JIRA-678 # docs: Update installation instructions in README
```

While this seems like a lot to think about for a simple commit message, getting into the habit of writing good commit messages will pay dividends later.

💡 **TIP** Tools such as [commitzen](https://commitizen-tools.github.io/commitizen/) can make creating commit messages a lot easier and in the future this may become a part of our standard toolkit.

## Pull Requests

## References
The following blogs were referenced in the creation of this content:
* [https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
* [https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
