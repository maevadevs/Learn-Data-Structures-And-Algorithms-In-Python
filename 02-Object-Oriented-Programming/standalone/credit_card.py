"""
Module: credit_card.py
This is a simple implementation of a CreditCard and PredatoryCreditCard classes.
"""

# IMPORT MODULES
# --------------
from decimal import Decimal
from typing import Final


# DEFINE CLASS
# ------------
class CreditCard:
    """A consumer credit card class."""

    def __init__(
        self,
        customer: str,
        bank: str,
        account: str,
        limit: Decimal,
        starting_balance: Decimal = Decimal(0),
    ) -> None:
        """Create a new credit card instance with zero initial balance (default).

        Args:
            - `customer` (`string`): The name of the customer.
            - `bank` (`string`): The name of the bank.
            - `account` (`string`): The account identifier.
            - `limit` (`Decimal`): The credit limit.
            - `starting_balance` (`Decimal`): The starting balance of the account.

        Returns:
            - `None`
        """
        self._customer: str = customer
        self._bank: str = bank
        self._account: str = account
        self._limit: Decimal = limit
        self._balance: Decimal = starting_balance

    def get_customer(self) -> str:
        """Return the name of the customer on the credit card.

        Args:
            - `None`

        Returns:
            - `str`: The name of the customer on the credit card.
        """
        return self._customer

    def get_bank(self) -> str:
        """Return the name of the bank on the credit card.

        Args:
            - `None`

        Returns:
            - `str`: The name of the bank on the credit card.
        """
        return self._bank

    def get_account(self) -> str:
        """Return the account identifier of the card as a string.

        Args:
            - `None`

        Returns:
            - `str`: The account identifier on the card.
        """
        return self._account

    def get_limit(self) -> Decimal:
        """Return the current limit of the credit card.

        Args:
            - `None`

        Returns:
            - `float`: The current limit of the credit card.
        """
        return self._limit

    def get_balance(self) -> Decimal:
        """Return the current balance of the credit card.

        Args:
            - `None`

        Returns:
            - `float`: The current balance of the credit card.
        """
        return self._balance

    def charge(self, price: Decimal) -> bool:
        """Charge given price to the card if there is sufficient credit limit.

        Args:
            - `price` (`Decimal`): The price of the item being charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed. `False` if charge was denied.
        """
        # If charge would exceed limit, cannot accept charge
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount: Decimal) -> None:
        """Process customer payment that reduces balance.

        Args:
            - `amount` (`float`): The amount that the customer is paying.

        Returns:
            - `None`
        """
        self._balance -= amount


# UNIT TESTS
# ----------
if __name__ == "__main__":
    # Variables
    wallet: list[CreditCard] = []

    # Append credit cards to the wallet
    wallet.append(
        CreditCard(
            "John Bowman", "California Savings", "5391 0375 9387 5309", Decimal(2500)
        )
    )
    wallet.append(
        CreditCard(
            "John Bowman", "California Federal", "3485 0399 3395 1954", Decimal(3500)
        )
    )
    wallet.append(
        CreditCard(
            "John Bowman", "California Finance", "5391 0375 9387 5309", Decimal(5000)
        )
    )

    # Test charge
    for val in range(1, 17):
        wallet[0].charge(Decimal(val))
        wallet[1].charge(2 * Decimal(val))
        wallet[2].charge(3 * Decimal(val))

    # Test methods on all credit cards
    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")

        while wallet[c].get_balance() > Decimal(100):
            wallet[c].make_payment(Decimal(100))
            print(f"New balance = {wallet[c].get_balance()}")

        print()


# DEFINE CLASS
# ------------
class PredatoryCreditCard(CreditCard):
    """An extension to `CreditCard` that compounds interest and fees."""

    def __init__(
        self, customer: str, bank: str, accnt: str, limit: Decimal, apr: Decimal
    ) -> None:
        """Create a new `PredatoryCreditCard` instance.

        Args:
            - `customer` (`str`): The name of the customer (e.g., John Bowman).
            - `bank` (`str`): The name of the bank (e.g., California Savings).
            - `acnt` (`str`): The acount identifier (e.g., 5391 0375 9387 5309).
            - `limit` (`float`): Credit limit (measured in dollars).
            - `apr` (`float`): Annual percentage rate (e.g., 0.0825 for 8.25% APR).

        The initial balance is zero.
        """
        # Call super constructor
        super().__init__(customer=customer, bank=bank, account=accnt, limit=limit)
        self._apr: Decimal = apr

    def charge(self, price: Decimal) -> bool:
        """Charge a given price to the card, assuming sufficient credit limit.

        Args:
            - `price` (`Decimal`): The price that is charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed, `False` and assess 5 fee if charge is denied.
        """
        # Call inherited method
        _success: bool = super().charge(price)

        if not _success:
            # Assess penalty
            self._balance += 5

        # Caller expects return value
        return _success

    def process_month(self) -> None:
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplicative factor
            monthly_factor: Decimal = Decimal(
                f"{pow(1 + self._apr, Decimal(1) / Decimal(12))}"
            )
            self._balance *= monthly_factor


# UNIT TESTS
# ----------
if __name__ == "__main__":
    # Variables
    wallet2: list[PredatoryCreditCard] = []

    # Append credit cards to the wallet
    wallet2.append(
        PredatoryCreditCard(
            "John Bowman",
            "California Savings",
            "5391 0375 9387 5309",
            Decimal(2500),
            Decimal("0.0825"),
        )
    )
    wallet2.append(
        PredatoryCreditCard(
            "John Bowman",
            "California Federal",
            "3485 0399 3395 1954",
            Decimal(3500),
            Decimal("0.0525"),
        )
    )
    wallet2.append(
        PredatoryCreditCard(
            "John Bowman",
            "California Finance",
            "5391 0375 9387 5309",
            Decimal(5000),
            Decimal("0.0225"),
        )
    )

    # Test charge
    for val in range(1, 17):
        wallet2[0].charge(Decimal(val))
        wallet2[1].charge(2 * Decimal(val))
        wallet2[2].charge(3 * Decimal(val))

    # Test methods on all credit cards
    for c in range(3):
        print(f"Customer = {wallet2[c].get_customer()}")
        print(f"Bank = {wallet2[c].get_bank()}")
        print(f"Account = {wallet2[c].get_account()}")
        print(f"Limit = {wallet2[c].get_limit()}")
        print(f"Balance (Before Month Processing) = {wallet2[c].get_balance()}")
        wallet2[c].process_month()
        print(f"Balance (After Month Processing) = {wallet2[c].get_balance()}")

        while wallet2[c].get_balance() > Decimal(100):
            wallet2[c].make_payment(Decimal(100))
            print(f"New balance = {wallet2[c].get_balance()}")

        print()


# DEFINE CLASS
# ------------
class PredatoryCreditCardV2(CreditCard):
    """An extension to `CreditCard` that compounds interest and fees."""

    # Class Data Members
    # ------------------
    _OVERLIMIT_FEE: Final[Decimal] = Decimal(5)

    # Class Methods
    # -------------
    def __init__(
        self, customer: str, bank: str, accnt: str, limit: Decimal, apr: Decimal
    ) -> None:
        """Create a new predatory credit card instance.

        Args:
            - `customer` (`str`): The name of the customer (e.g., John Bowman).
            - `bank` (`str`): The name of the bank (e.g., California Savings).
            - `accnt` (`str`): The acount identifier (e.g., 5391 0375 9387 5309).
            - `limit` (`float`): Credit limit (measured in dollars).
            - `apr` (`float`): Annual percentage rate (e.g., 0.0825 for 8.25% APR).

        The initial balance is zero.
        """
        super().__init__(customer, bank, accnt, limit)  # call super constructor
        self._apr: Decimal = apr

    def charge(self, price: Decimal) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            - `price` (`float`): The price that is charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed, `False` and assess 5 fee if charge is denied.
        """
        # Call inherited method
        _success: bool = super().charge(price)

        if not _success:
            # Assess penalty
            self._balance += PredatoryCreditCardV2._OVERLIMIT_FEE

        # Caller expects return value
        return _success

    def process_month(self) -> None:
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplicative factor
            monthly_factor: Decimal = Decimal(
                f"{pow(1 + self._apr, Decimal(1) / Decimal(12))}"
            )
            self._balance *= monthly_factor
