import pytest
from src.bank_account import BankAccount


@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_ammounts(ammount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected


# TODO: Create a test that does't allow the deposit to be less than zero
def test_deposit_less_than_zero():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)