import sys
import threading
import time
import unittest

from guild_bank import GuildBank


class GuildBankAccountTest(unittest.TestCase):
    def test_that_a_newly_opened_account_has_zero_balance(self):
        account = GuildBank()
        account.open_account()
        self.assertEqual(account.get_balance(), 0)

    def test_can_deposit_gold(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(100)
        self.assertEqual(account.get_balance(), 100)

    def test_can_deposit_gold_sequentially(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(100)
        account.deposit_gold(50)

        self.assertEqual(account.get_balance(), 150)

    def test_can_withdraw_gold(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(100)
        account.withdraw_gold(50)

        self.assertEqual(account.get_balance(), 50)

    def test_can_withdraw_gold_sequentially(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(100)
        account.withdraw_gold(20)
        account.withdraw_gold(80)

        self.assertEqual(account.get_balance(), 0)

    def test_checking_balance_of_closed_account_throws_error(self):
        account = GuildBank()
        account.open_account()
        account.close()

        with self.assertRaisesWithMessage(ValueError):
            account.get_balance()

    def test_deposit_into_closed_account(self):
        account = GuildBank()
        account.open_account()
        account.close()

        with self.assertRaisesWithMessage(ValueError):
            account.deposit_gold(50)

    def test_withdraw_from_closed_account(self):
        account = GuildBank()
        account.open_account()
        account.close()

        with self.assertRaisesWithMessage(ValueError):
            account.withdraw_gold(50)

    def test_close_already_closed_account(self):
        account = GuildBank()
        with self.assertRaisesWithMessage(ValueError):
            account.close()

    def test_open_already_opened_account(self):
        account = GuildBank()
        account.open_account()
        with self.assertRaisesWithMessage(ValueError):
            account.open_account()

    def test_reopened_account_does_not_retain_balance(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(50)
        account.close()
        account.open_account()
        self.assertEqual(account.get_balance(), 0)

    def test_cannot_withdraw_more_than_deposited(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(25)

        with self.assertRaises(ValueError):
            account.withdraw_gold(50)

    def test_cannot_withdraw_negative(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(100)

        with self.assertRaisesWithMessage(ValueError):
            account.withdraw_gold(-50)

    def test_cannot_deposit_negative(self):
        account = GuildBank()
        account.open_account()

        with self.assertRaisesWithMessage(ValueError):
            account.deposit_gold(-50)

    def test_can_handle_concurrent_transactions(self):
        account = GuildBank()
        account.open_account()
        account.deposit_gold(1000)

        self.adjust_balance_concurrently(account)

        self.assertEqual(account.get_balance(), 1000)

    def adjust_balance_concurrently(self, account):
        def transact():
            account.deposit_gold(5)
            time.sleep(0.001)
            account.withdraw_gold(5)

        try:
            sys.setswitchinterval(1e-12)
        except AttributeError:
            sys.setcheckinterval(1)

        threads = [threading.Thread(target=transact) for _ in range(1000)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()


