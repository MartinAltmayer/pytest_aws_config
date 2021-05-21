To run the tests, this directory must contain a file 'credentials' with valid credentials
for an IAM user (or role). The tests will only assume the role (to check whether credentials
are available or not), they won't do any AWS calls.

See https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for the format.
