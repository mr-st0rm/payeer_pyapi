# payeer_api
Connecting the Payeer payment system to your product

<h3>Guide on connecting Payeer to your system</h3>

Each response from the Payeer server necessarily contains the auth_error field, which shows whether the authentication parameters are specified correctly. The response to the request also contains an array of errors, which indicates the presence of errors in the execution of the request.
>If you have any questions about these errors, [look here]()

<h3>Getting started with the API</h3>
To work with the API, you need to go to your personal [account](https://payeer.com/ru/account/?tab=api) click on the "Activation" button in the right column.<br>
Fill in the user name, generate a secret key for working with the API and for additional security, enter the IP address from which you will send requests to the Payeer server.
:exclamation:Attention<br> 
__Do not tell anyone the secret key for the API.After adding the API, you are given a user ID that you need to use, together with the key and account number, for authentication in requests.__

<h3>FAQ</h3>
1. When requesting the API, I get the error "auth error: account or apiId or apiPass is incorrect or api-user was blocked"
> Check the correctness of the account number, user-id and secret key, as well as the disabled blocking of the user in the settings of mass payments.
2. I can't get rid of the error "IP 1.2.3.4 does not satisfy the security settings"
> Specify the IP that is returned in error in the settings of mass payments and repeat the request.After a while, the error "AUTH error: account or apiId or apiPass is incorrect or api-user was blocked" appears again, although no settings have been changed.
