import pytest
from wallet_box.wallet import Wallet, InsufficientFunds


@pytest.fixture()
def empty_wallet():
    return Wallet()


@pytest.fixture()
def wallet():
    return Wallet(20)


def test_add_wallet(wallet):
    wallet.add_cash(90)
    assert wallet.balance == 110


def test_spend_wallet(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_raise_exception_on_not_enough_funds_to_spend(empty_wallet):
    with pytest.raises(InsufficientFunds):
        empty_wallet.spend_cash(100)
