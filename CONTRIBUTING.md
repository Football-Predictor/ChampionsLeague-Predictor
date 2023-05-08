<div align="center">
  <h1>Contributing</h1>
</div>

## Table of Contents
- [Introduction](#introduction-star)
- Development
  - [Project Setup](#project-setup-hammer) 
  - [Contribute Code](#code-contribution-construction)

## Introduction :star:
This guide should serve as a set of guidelines and instructions for all contributors with respect to how they can participate and improve the project.

The purpose of this guide is to establish a clear and consistent process for contributing to the project. This guide outlines how to setup the project locally, submit issues, branching conventions submit and review pull requests.

## Project Setup :hammer:
Follow these instructions if you **do not** have permissions to edit the remote repository.

> **Note**:
> This project uses GitHub Pull Requests to manage contributions, so [read up on how to fork a GitHub project and file a PR](https://guides.github.com/activities/forking) if you've never done it before

> **Install dependencies**
```sh
$ pip install -r requirements.txt
```
## Code Contribution :construction:

We welcome all contributions to the project. Follow the step-by-step guide below to ensure your contribution fits the required standard and can be added to the project!

### **To contribute code**:
- [Set up the project](#project-setup-hammer).
- Identify any required modifications in the source code. 

- Create and checkout a new branch.
  - `git checkout -b <token/summary/ticket_number>`
  - Tokens that should be used:
    Token Type | Description
    --- | --- 
    `feat`| This is a new feature
    `refac`| This is for refactoring an existing feature
    `bug`| This is for a bug fix
    `doc`| This is for creating & editing documentation
    `test`| This is a branch used for experimenting
  - Your summary should be 2-3 words or less and separated by dashes.
  - Your ticket number can be found in the issues / projects tab of the repo.
  - Example:
    - `git checkout -b refac/readme-update/1`

- Implement these changes accordingly.
- Incorporate supplementary documentation as needed to support the modifications made.

- Add modified code for staging
  - `git add <path/to/file>`
  - Note: Add each changed file individually. This will allow for better tracking of issues.

- Commit a staged file with a descriptive message
  - `git commit -m "your message"`
  - Guidelines for writing a commit message:
    -  You should use the [imperative mood](https://git.kernel.org/pub/scm/git/git.git/tree/Documentation/SubmittingPatches?id=HEAD#n183) for writing your commit messages.
    - Additional resource: https://initialcommit.com/blog/Git-Commit-Message-Imperative-Mood
    - Example:
      - `git commit -m "Update README"`
    - Typical commit messages begin with: `Add`, `Update`, `Delete`, `Refactor` and so forth.

- Once you are satisfied with your contribution, go to [Pull Requests](https://github.com/Football-Predictor/BallondOr-Predictor/pulls) and open a new pull request with your changes.
- A maintainer or specified reviewer will be assigned to verify and test your changes.

> **Warning**:
> If your contribution does not align with the instructions above, it will not be acknowledged. 

<div align="right">
  <h6>Author: <a href="https://github.com/steventohme">Steven Tohme</a> (24/04/2023)</h6>
</div>