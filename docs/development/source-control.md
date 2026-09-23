# Source Control Development Workflow

## Purpose

Use an isolated Git worktree for feature development. The branch relationship
is established first; the workspace is then attached to that feature branch.
This keeps the primary checkout available for coordination and prevents
uncommitted work in one task from leaking into another.

The intended relationship is:

    origin/master
        └── dev
            └── feature/<feature-name>
                    └── .workspace/<feature-name>

A worktree is a checkout of a branch. It is not the parent of the branch and
does not replace the branch hierarchy.

## Preconditions

Before creating a feature workspace:

1. Identify the owning repository.
2. Fetch current remote refs.
3. Confirm the intended base branch and commit.
4. Confirm that the feature branch and workspace path do not already exist.
5. Keep unrelated dirty work in the primary checkout out of the feature branch.

Run:

```bash
git fetch origin --prune
git branch -a -vv
git worktree list
```

If `dev` does not exist, stop and choose its initial commit explicitly. Do not
silently substitute another branch. When the operator has chosen
`origin/master` as the initial base, create the local branch without assigning
`origin/master` as its long-term upstream:

```bash
git branch --no-track dev origin/master
```

Publishing `dev` is a separate repository-owner decision.

## Create a Feature Workspace

Use a short, task-specific feature name. The following example uses
`v0-ingestor-pilot`.

First create the feature branch from `dev`:

```bash
git branch feature/v0-ingestor-pilot dev
```

Then attach a worktree to that feature branch:

```bash
git worktree add \
  .workspace/v0-ingestor-pilot \
  feature/v0-ingestor-pilot
```

Git also supports an atomic equivalent:

```bash
git worktree add \
  -b feature/v0-ingestor-pilot \
  .workspace/v0-ingestor-pilot \
  dev
```

The two forms produce the same branch ancestry. Prefer the explicit two-step
form when reviewing or teaching the process because it makes the branch and
workspace responsibilities visible.

## Keep the Workspace Local

A nested `.workspace/` contains Git worktree administration and checked-out
files. It is operational state, not repository content. Exclude it locally:

```bash
grep -qxF '.workspace/' .git/info/exclude || \
  printf '\n.workspace/\n' >> .git/info/exclude
```

Use `.git/info/exclude` when the workspace convention is local to the operator.
Use a tracked `.gitignore` entry only when the repository has explicitly
adopted `.workspace/` as a shared convention.

Do not copy the primary checkout into `.workspace/`. Do not copy unrelated
uncommitted files into the feature worktree. Transfer an intentional change
with a reviewed commit or patch when it belongs to the feature.

## Verify the Workspace

Confirm the branch, base, and worktree registration:

```bash
git branch -vv
git worktree list
git -C .workspace/v0-ingestor-pilot status --short --branch
git merge-base --is-ancestor \
  dev \
  feature/v0-ingestor-pilot
```

The final command must exit successfully. Record the base commit when handing
the task to another session or operator.

## Develop and Validate

Make feature changes only inside the feature worktree:

```bash
cd .workspace/v0-ingestor-pilot
```

Before committing:

1. Review `git status` and `git diff`.
2. Run the repository's focused tests.
3. Run the required lint and type checks.
4. Confirm that generated files, credentials, caches, and workspace state are
   not staged.
5. Commit only the bounded feature changes.

Publish the feature branch explicitly when it is ready for remote review:

```bash
git push --set-upstream origin feature/v0-ingestor-pilot
```

## Integrate

The feature branch integrates into `dev`, not directly into `master`, unless
the repository owner explicitly chooses another release process.

Before integration, update the feature from the current `dev` according to the
repository's merge or rebase policy, rerun validation, and inspect the final
diff from the merge base:

```bash
git diff dev...feature/v0-ingestor-pilot
```

A later release promotes accepted `dev` state to `master`. Creating a worktree
does not itself authorize a merge, push, or release.

## Remove the Workspace

After the feature has been integrated and any needed evidence is durable in
Git, remove the worktree from the primary checkout:

```bash
git worktree remove .workspace/v0-ingestor-pilot
git worktree prune
```

Delete the local feature branch only after confirming integration:

```bash
git branch -d feature/v0-ingestor-pilot
```

Delete `dev` only if the repository is abandoning the development-branch
workflow. Never remove a worktree directory manually while Git still registers
it.
