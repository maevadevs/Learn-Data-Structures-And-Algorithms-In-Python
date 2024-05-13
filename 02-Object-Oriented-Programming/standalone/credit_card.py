"""
Module: credit_card.py
This is a simple implementation of a CreditCard and PredatoryCreditCard classes.
"""

# IMPORT MODULES
# --------------
from typing import Final


# DEFINE CLASS
# ------------
class CreditCard:
    """A consumer credit card class"""

    def __init__(
        self,
        customer: str,
        bank: str,
        account: str,
        limit: float,
        starting_balance: float = 0,
    ) -> None:
        """Create a new credit card instance with zero initial balance (default).

        Args:
            - `customer` (`string`): The name of the customer
            - `bank` (`string`): The name of the bank
            - `account` (`string`): The account identifier
            - `limit` (`float`): The credit limit
            - `starting_balance` (`float`): The starting balance of the account

        Returns:
            - `None`
        """
        self._customer: str = customer
        self._bank: str = bank
        self._account: str = account
        self._limit: float = limit
        self._balance: float = starting_balance

    def get_customer(self) -> str:
        """Return the name of the customer on the credit card.

        Args:
            - `None`

        Returns:
            - `str`: The name of the customer on the credit card
        """
        return self._customer

    def get_bank(self) -> str:
        """Return the name of the bank on the credit card.

        Args:
            - `None`

        Returns:
            - `str`: The name of the bank on the credit card
        """
        return self._bank

    def get_account(self) -> str:
        """Return the account identifier of the card as a string.

        Args:
            - `None`

        Returns:
            - `str`: The account identifier on the card
        """
        return self._account

    def get_limit(self) -> float:
        """Return the current limit of the credit card.

        Args:
            - `None`

        Returns:
            - `float`: The current limit of the credit card.
        """
        return self._limit

    def get_balance(self) -> float:
        """Return the current balance of the credit card.

        Args:
            - `None`

        Returns:
            - `float`: The current balance of the credit card.
        """
        return self._balance

    def charge(self, price: float) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            - `price` (`float`): The price of the item being charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed. `False` if charge was denied.
        """
        # if charge would exceed limit, cannot accept charge
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount: float) -> None:
        """Process customer payment that reduces balance.

        Args:
            - `amount` (`float`): The amount that the customer is paying

        Returns:
            - `None`
        """
        self._balance -= amount


# DEFINE CLASS
# ------------
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    # Class Data Members
    # ------------------
    OVERLIMIT_FEE: Final[float] = 5.00

    # Class Methods
    # -------------
    def __init__(
        self, customer: str, bank: str, acnt: str, limit: float, apr: float
    ) -> None:
        """Create a new predatory credit card instance.

        Args:
            - `customer` (`str`): The name of the customer (e.g., John Bowman )
            - `bank` (`str`): The name of the bank (e.g., California Savings )
            - `acnt` (`str`): The acount identifier (e.g., 5391 0375 9387 5309 )
            - `limit` (`float`): Credit limit (measured in dollars)
            - `apr` (`float`): Annual percentage rate (e.g., 0.0825 for 8.25% APR)

        The initial balance is zero.
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr: float = apr

    def charge(self, price: float) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            - `price` (`float`): The price that is charged to the credit card

        Returns:
            - `bool`: `True` if charge was processed, `False` and assess 5 fee if charge is denied
        """
        _success: bool = super().charge(price)  # call inherited method

        if not _success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE  # assess penalty

        return _success  # caller expects return value

    def process_month(self) -> None:
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor: float = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor


# UNIT TESTS
# ----------
if __name__ == "__main__":
    # Variables
    wallet: list[CreditCard] = []

    # Append credit cards to the wallet
    wallet.append(
        CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000)
    )

    # Test charge
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    # Test methods on all credit cards
    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f"New balance = {wallet[c].get_balance()}")

        print()
