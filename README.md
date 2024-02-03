# Notes
- `Utils` Add functions that you use frequently  
- `@ensure_annotations` Decorator to ensure that the return value is of the same type
- `git tag <tag name>`This is used to save the project with a specific version like v0.0
- `git release`Used to release the specific tag with additional compiled binary files  create tag as `git tag v1.1.-rc1` and after make this release in GitHub 
- `@classmethod` is only available for the class but not for the instance of class
- `@staticmethod` does not require any information of the instance. like in simple term not require self argument
- `git merge --squash <brnach name>`
- `git rebase <branch name>`
- `@property` This is for the hidden function and we can access the hidden function with the parenthesis 
- `os.path.dirname` It will ignore the last filename and return the remaining path
- The `Pipeline` Pipeline is before the training. Callback is during the training that's why we haven't made any separate pipeline
# Hot-fix in specific commit
- `git tag` find where the bug is
- `git checkout -b hotfix-branch tag-name` create branch for that fix in specific tag 
- `git push origin hotfix-branch` pull request for that hotfix
- `git tag hotfix-version` creates the bug-fixed tag
- `git push origin hotfix-version` push the bug fixed tag


# End-to-End Deep Learning Project

# Workflow
- update config.yaml
- update secret.yaml [optional]
- update param.yaml 
- update the entity
<!-- update Model parameters -->
- Update entity
Whenever you create a method, entity is that what is the written type of that 
- update the configuration manager in src  config
- update the components
- update the pipeline
- updat the main.py
