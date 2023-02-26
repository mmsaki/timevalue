import re


def format_branch_name(name):
    # If branch has name like "bugfix/issue-1234-bug-title", take only "1234" part
    pattern = re.compile("^(bugfix|feature)\/issue-(?P<branch>[0-9]+)-\S+")

    match = pattern.search(name)
    if match:
        return match.group("branch")

    # function is called even if branch name is not used in a current template
    # just left properly named branches intact
    if name in ["master", "dev"]:
        return name

    # fail in case of wrong branch names like "bugfix/issue-unknown"
    raise ValueError(f"Wrong branch name: {name}")


def format_tag_name(name):
    # If tag has name like "release/1.2.3", take only "1.2.3" part
    pattern = re.compile(r"release\/(?P<tag>[^\d.]+)")

    match = pattern.search(name)
    if match:
        return match.group("tag")

    # just left properly named tags intact
    if name.startswith("v"):
        return name

    # fail in case of wrong tag names like "release/unknown"
    raise ValueError(f"Wrong tag name: {name}")
