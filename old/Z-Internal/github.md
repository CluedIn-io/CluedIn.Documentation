#  Working in Github

##  Inner Sourcing Approach

For transparency purpose, anyone can view the code and P-R from any teams. If you see a mistake in one of the repo:

1. Create an Issue describing the Error.

If you can fix the Error yourself:

2. Create a branch with appropriate name (see below for branch naming)
3. Fix in your branch.
4. Create a Pull Request.
5. Wait for Code Review.

## Code Review Practises

[Code Review Guidelines](./review.md)

## Pull Request Practises

1. Reviewer gives review fowlling code review guidlines.
2. Once approved, P-R owner `squash` the P-R with a relevant comment
3. P-R owner `delete the branch`

## Branching Stategy

We use [Github Flow](https://guides.github.com/introduction/flow/), a very lightwight branch-based workflow.

**Branch Name**

Before branching, make sure you have created an Issue describing the work you are doing. It will be easier for the code review to understand what you are working on.

`bugfix`

If you are only fixing a small bug, please use `/bugfix/[github-issue]-[shortDescription]`

`feature`

If you work on a specific feature `/feature/[github-issue]-[shortDescription]`

`EPIC`

EPIC is created when you need multiple features to be finished before doing a proper P-R.

EPIC will become the main branch where developer will need to P-R before making the P-R back to master repo. Naming strategy: `/feature/[github-issue]-[shortDescription]`


