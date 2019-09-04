Removing Data for an existing account

You might need to reset your account for many reasons. You could either reset your entire CluedIn instance, create a new account, or reset a particular account. 

A reset of an account will remove all data except the initial 2 records of a User and Account that are created when creating a new CluedIn account. 

You will need to use our REST API, and be an Administrator to be able to run this particular REST command. You will need to supply the OrganizationId of the account that you would like to reset. 

Note: On developer machines, it may be easiest to use the Docker option to simply reset your volumes to a default installation of CluedIn. 