import typing
import requests

from .exceptions import PayeerAPIException


class PayeerApi:
    __request_url = "https://payeer.com/ajax/api/api.php"
    __headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def __init__(self, account: str, api_id: int, api_pass: str):
        self.__account = account
        self.__api_id = api_id
        self.__api_pass = api_pass

        self._check_account()

    def _check_account(self) -> typing.Dict:
        """
        Check that Payeer account is available

        :return: Dictionary auth_error and errors
            auth_error = 0, means that authorized
            auth_error = 1, account or apiId or apiPass is incorrect or api-user was blocked
            auth_error = 2, IP 1.2.3.4 does not satisfy the security settings
        """
        return self._send_request()

    def _send_request(self, **kwargs) -> typing.Dict:
        kwargs.update({
            'account': self.__account,
            'apiId': self.__api_id,
            'apiPass': self.__api_pass
        })

        response = requests.post(self.__request_url, kwargs, headers=self.__headers).json()

        if errors := response.get('errors'):
            raise PayeerAPIException(errors)

        return response

    def get_balance(self) -> typing.Dict:
        """
        Check account balance data

        :return: dictionary with currencies and their balances (total, available, hold)
        """
        return self._send_request(action="getBalance").get("balance")

    def transfer_cash(self, transfer_sum: typing.Union[int, float], transfer_to: str, cur_in: str = "RUB",
                      cur_out: str = "RUB", comment: str = None) -> int:
        """
        Send cash to another wallet in Payeer system

        :param transfer_sum: the amount of debiting (the amount of crediting will be calculated automatically with
            deduction of all commissions from the recipient)
        :param transfer_to: recipient's wallet number
        :param cur_in: the currency to be debited from (USD, EUR, RUB)
        :param cur_out: currency of crediting (in case of a difference in the currency of debiting from the
            currency of crediting, the conversion will be made automatically at the rate of the Payeer system
             at the time of transfer)
        :param comment: payment comment
        :return: historyId transaction number
        """
        send_account_data = {
            "action": "transfer",
            "curIn": cur_in,
            "sum": transfer_sum,
            "curOut": cur_out,
            "to": transfer_to,
        }
        if comment:
            send_account_data.update(comment=comment)

        return self._send_request(**send_account_data).get("historyId")

    def check_wallet_available(self, wallet: str) -> bool:
        """
        Check user's wallet is available

        :param wallet: user's wallet number in Payeer
        :return: True if exists
        """
        try:
            self._send_request(action="checkUser", user=wallet)
        except PayeerAPIException:
            return False

        return True

    def conversion_rates(self, output: str = "Y") -> typing.Dict:
        """
        The conversion takes place according to the internal Payeer rates, which can be obtained using this method.

        :param output: choosing the direction of conversion rates (N - get entry courses, Y - get withdrawal rates)
        :return: dictionary with all rates
        """
        return self._send_request(action="getExchangeRate", output=output).get("rate")

    def payout(self, sum_in: typing.Union[int, float], to_wallet: str, cur_in: str = "RUB", cur_out: str = "RUB",
               payout_system_id: str = "1136053") -> int:
        """
        Payment to any payment system supported by Payeer. You can view the list of payment systems on
        the corresponding tab in the API user settings or using the special available_payment_systems method

        :param sum_in: amount withdrawn (the amount deposited will be calculated automatically,
            factoring in all fees from the recipient)
        :param to_wallet: recipient's account number in the selected payment system
        :param cur_in: currency with which the withdrawal will be performed
        :param cur_out: deposit currency
        :param payout_system_id: ID of selected payment system, default Payeer
        :return: history id
        """
        return self._send_request(action="payout", ps=payout_system_id, sumIn=sum_in, curIn=cur_in, curOut=cur_out,
                                  param_ACCOUNT_NUMBER=to_wallet).get("historyId")

    def available_payment_systems(self) -> typing.Dict:
        """
        The method returns a list of payment systems available for withdrawal.

        :return: dictionary with payment systems for withdraw
        """
        return self._send_request(action="getPaySystems").get("list")

    def transactions_history(self, count: int = 10, sort: str = "desc", transaction_type: str = None) -> typing.List:
        """
        Get account transactions history

        :param count: count of transactions, default 10
        :param sort: sorting by date (default desc), can be asc.
            The ASC parameter sets the sort order in ascending
            order, from smaller values to larger ones.
            The DESC parameter sets the sort order in descending order,
            from large values to smaller ones.
        :param transaction_type: incoming or outgoing
        :return: list with all transaction
        """
        send_account_data = {
            "sort": sort,
            "count": count
        }
        if transaction_type:
            send_account_data.update(type=transaction_type)

        return self._send_request(action="history", **send_account_data).get("history")
