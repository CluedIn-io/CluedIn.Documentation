Creating an Account

One can create many CluedIn accounts per CluedIn instance. This can be used for multi-tenancy, or simply for testing different things out. 

When CluedIn is first installed, you will not have a default account created. You will need to use the REST API or the User Interface to be able to register your account. You will need to produce the following information:

- Account Name
- Email Address (unique per instance of CluedIn)
- User Name
- Password
- Account Subdomain

Once an account is created, you will be given an empty CluedIn account with 2 pieces of existing data. You will have a record for your User and a record for the Account that you created. 

If creating subsequent accounts, they must have unique values than the ones previously used, except the password (that can be the same).

You can signup by visiting the following Url of your CluedIn installation : https://app.<<insert your domain>>/signup