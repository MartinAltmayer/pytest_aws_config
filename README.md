# pytest_aws_config

Tiny [Pytest](https://pytest.org) plugin that mocks your AWS configuration in tests, making your tests independent of the configuration on the developer machine. In particular, it prevents your tests from accessing your AWS credentials.

## Why is this useful?

Developers often use AWS configuration files to store (temporary) credentials to IAM users/roles. This is very useful to access the AWS account from the command line. But it also means that tests will run with these credentials.

```
> export AWS_PROFILE=production
> aws logs describe-log-groups  # analyze some issue on production
> ... time passes ...
> ... write some code ...
> pytest tests  # execute tests
```
Whoops! These tests just ran with access to your production account. Hopefully everything was correctly mocked or patched.

## Installation

Just install this plugin with `pip install pytest_aws_config`. No configuration necessary.

## What about functional tests?

Of course, some of your tests may actually need AWS credentials. You have two options:

- Disable the plugin when running functional tests: `pytest -p no:pytest_aws_config`
- Keep the plugin and use some other mechanism (e.g. a pytest fixture) to set the configuration in the test. Then your tests remain independent of the configuration on the developer machine.

## Links

AWS documentation on [configuration files](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) and [environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).
