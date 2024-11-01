1: Sign in to AWS Management Console

    Go to the https://aws.amazon.com/console/.
    Sign in with your AWS account.

2: Navigate to IAM (Identity and Access Management)

    In the AWS Management Console, search for IAM in the search bar and select it.
    This will take you to the IAM dashboard.

3: Create a New IAM User

    Click on Users in the left sidebar.
    Click the Add user button.
    Enter a username (e.g., my-django-username).
    Under Access type, check the box for Programmatic access. This will generate an Access Key ID and Secret Access Key.

4: Set Permissions

    Click Next: Permissions.
    You can attach existing policies directly or create a new policy for your user. For S3 access, you might use the AmazonS3FullAccess policy or create a custom policy with specific permissions.
    After setting permissions, click Next: Tags (you can optionally add tags).
    Click Next: Review, and then click Create user.

5: Download Your Credentials

    After creating the user, you will see a success message.
    This page will show you your Access Key ID and Secret Access Key. 
    Download the .csv file or copy these keys to a secure location. 
    You will not be able to see the Secret Access Key again after this point.
