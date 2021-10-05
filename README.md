### payeer_api
Connecting the Payeer payment system to your product

### Guide on connecting Payeer to your system
---

Each response from the Payeer server necessarily contains the auth_error field, which shows whether the authentication parameters are specified correctly. The response to the request also contains an array of errors, which indicates the presence of errors in the execution of the request.
>If you have any questions about these errors, [look here](https://github.com/St0rm1k/payeer_api/blob/main/README.md#faq)

### Getting started with the API
To work with the API, you need to go to your personal [account](https://payeer.com/ru/account/?tab=api) click on the "Activation" button in the right column.  
Fill in the user name, generate a secret key for working with the API and for additional security, enter the IP address from which you will send requests to the Payeer server.  

### :exclamation:Attention  
**Do not tell anyone the secret key for the API.After adding the API, you are given a user ID that you need to use, together with the key and account number, for authentication in requests.**

### Examples  
---
Let's try to check the validity of the wallet

```
from payeer_api import PayeerApi

wallet = "P10000000000"

app = PayeerApi(account="P100101010", api_id=12345678, api_pass="SecretKey")

print(app.check_wallet_available(wallet))

Output -> False

```

Let's try to get automatic conversion rates by default get withdrawal rates
```
print(app.conversion_rates())

Output -> {'RUB/USD': '0.01307531', 'RUB/EUR': '0.01127733', 'USD/RUB': '68.94017', 'USD/EUR': '0.81903631', 'EUR/USD': '1.10190475', 'EUR/RUB': '79.963685'}
```
If we change `output` parameter, we get entry courses
```
print(app.conversion_rates(output="N"))

Output -> {'RUB/USD': '0.01446907', 'RUB/EUR': '0.01247441', 'USD/RUB': '76.2888', 'USD/EUR': '0.90561469', 'EUR/USD': '1.21740517', 'EUR/RUB': '88.45179'}
```


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
* My website was hacked and all the money was withdrawn through the API
> For additional security, you can use a second account for payments, where you can keep the amount necessary for transfers in the short term. Please do not neglect the security audits of your site.

