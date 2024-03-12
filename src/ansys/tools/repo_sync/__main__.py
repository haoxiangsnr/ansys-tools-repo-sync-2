"""Tool to copy the content of one repo toward an other.

Run with:

.. code::

    repo-sync \
      --token <token> \
      --owner <organization-name> \
      --repository <repository-name> \
        --from-path-list <path1> --from-path-list <path2> \
            --to-path-list <path1> --to-path-list <path2> \
      --include-manifest <path-to-manifest>
      --branch_checked_out <branch-name>
      --new-branch-name <branch-name>
      --pr-title <pr-title>
"""

import click

from .repo_sync import synchronize as _synchronize


@click.command(short_help="Copy the content of a repository into an other repository.")
@click.option(
    "--owner", "-o", type=str, help="Name of the owner or organization.", required=True
)
@click.option(
    "--repository", "-r", type=str, help="Name of the repository.", required=True
)
@click.option("--token", "-t", type=str, help="Personal access token.", required=True)
@click.option(
    "--from-path-list",
    "-f",
    multiple=True,
    type=str,
    required=True,
)
@click.option(
    "--to-path-list",
    "-t",
    multiple=True,
    type=str,
    required=True,
)
@click.option(
    "--include-manifest",
    "-m",
    type=click.Path(dir_okay=False, exists=True),
    help="Manifest to mention accepted extension files.",
    required=True,
)
@click.option(
    "--branch_checked_out", "-b", type=str, help="Branch to check out.", default="main"
)
@click.option(
    "--clean-to-dir",
    is_flag=True,
    default=False,
    help="Clean the folder defined in --to-dir before synchronizing.",
)
@click.option(
    "--clean-to-dir-based-on-manifest",
    is_flag=True,
    default=False,
    help=(
        "Deletion of target directory is performed based on manifest file"
        " (i.e. only those files matching the extensions on it are deleted)."
        " Only has an effect if --clean-to-dir is passed."
    ),
)
@click.option(
    "--dry-run",
    "-d",
    is_flag=True,
    default=False,
    help="Simulate the behavior of the synchronization without performing it.",
)
@click.option(
    "--skip-ci",
    is_flag=True,
    default=False,
    help="Adds a ``[skip ci]`` prefix to the commit message or not.",
)
@click.option(
    "--random-branch-name",
    is_flag=True,
    default=False,
    help="Generates a random branch name instead of the typical ``sync/file-sync``. Used for testing purposes mainly.",
)
@click.option(
    "--new-branch-name",
    type=str,
    help="Name of the branch to create for the synchronization.",
    default="sync/file-sync",
)
@click.option(
    "--pr-title",
    type=str,
    help="Title of the pull request.",
    default="sync: file sync performed by ansys-tools-repo-sync",
)
def synchronize(
    owner,
    repository,
    token,
    from_path_list,
    to_path_list,
    include_manifest,
    branch_checked_out,
    clean_to_dir,
    clean_to_dir_based_on_manifest,
    dry_run,
    skip_ci,
    random_branch_name,
    new_branch_name,
    pr_title,
):
    """CLI command to execute the repository synchronization."""
    _synchronize(
        owner=owner,
        repository=repository,
        token=token,
        from_path_list=from_path_list,
        to_path_list=to_path_list,
        clean_to_dir=clean_to_dir,
        clean_to_dir_based_on_manifest=clean_to_dir_based_on_manifest,
        include_manifest=include_manifest,
        branch_checked_out=branch_checked_out,
        dry_run=dry_run,
        skip_ci=skip_ci,
        random_branch_name=random_branch_name,
        new_branch_name=new_branch_name,
        pr_title=pr_title,
    )


if __name__ == "__main__":
    synchronize()
