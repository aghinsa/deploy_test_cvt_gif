import os
import shlex
import re
import tempfile


def fake_clone_git_repo(*args, **kwargs):
    directory = tempfile.mkdtemp(prefix="test_deploy")
    dockerfile_content = (
        "# Usage\n" + "# docker run -d test/deploy\n" + "# \n" + "FROM ALPINE"
    )
    with open("../Dockerfile", "w+") as dockerfile:
        dockerfile.write(dockerfile_content)
    return {
        "repo": {
            "URL": "github.com/test/deploy",
            "directory": tempfile.mkdtemp(prefix="test_deploy"),
        }
    }


fake_clone_git_repo()
