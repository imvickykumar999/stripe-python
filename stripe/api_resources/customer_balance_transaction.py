from __future__ import absolute_import, division, print_function

from stripe.api_resources.customer import Customer
from stripe.api_resources.abstract import APIResource
from urllib.parse import quote_plus


class CustomerBalanceTransaction(APIResource):
    OBJECT_NAME = "customer_balance_transaction"

    def instance_url(self):
        base = Customer.class_url()
        cust_extn = quote_plus(self.customer)
        extn = quote_plus(self.id)
        return "%s/%s/balance_transactions/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a Customer Balance Transaction without a Customer ID. "
            "Use Customer.retrieve_customer_balance_transaction('cus_123', 'cbtxn_123')"
        )
