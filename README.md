### payeer_api
Connecting the Payeer payment system to your product

### Guide on connecting Payeer to your system

Each response from the Payeer server necessarily contains the auth_error field, which shows whether the authentication parameters are specified correctly. The response to the request also contains an array of errors, which indicates the presence of errors in the execution of the request.
>If you have any questions about these errors, [look here](https://github.com/St0rm1k/payeer_api/blob/main/README.md#faq)

### Getting started with the API
To work with the API, you need to go to your personal [account](https://payeer.com/ru/account/?tab=api) click on the "Activation" button in the right column.  
Fill in the user name, generate a secret key for working with the API and for additional security, enter the IP address from which you will send requests to the Payeer server.  
:exclamation:Attention  
**Do not tell anyone the secret key for the API.After adding the API, you are given a user ID that you need to use, together with the key and account number, for authentication in requests.**

### FAQ

* When requesting the API, I get the error "auth error: account or apiId or apiPass is incorrect or api-user was blocked"  
> Check the correctness of the account number, user-id and secret key, as well as the disabled blocking of the user in the settings of mass payments.
* I can't get rid of the error "IP 1.2.3.4 does not satisfy the security settings"  
> Specify the IP that is returned in error in the settings of mass payments and repeat the request.
* After a while, the error "AUTH error: account or apiId or apiPass is incorrect or api-user was blocked" appears again, although no settings have been changed  
> After a certain number of authorization attempts with an incorrect api secret key, the user is blocked, you can unlock it in the settings of mass payments. You may not have changed the secret key in all places on your site, or someone is trying to find a password for your API:
  1. Delete the old api user
  2. Create a new one with IP protection
  3. Write down the new access data on your website
