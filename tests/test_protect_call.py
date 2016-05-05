import time
import unittest
import common

from trezorlib import messages_pb2 as proto
from trezorlib import types_pb2 as types
from trezorlib.client import PinException, CallException

# FIXME TODO Add passphrase tests

class TestProtectCall(common.TrezorTest):

    def _some_protected_call(self, button, pin, passphrase):
        # This method perform any call which have protection in the device
        res = self.client.ping('random data',
                                button_protection=button,
                                pin_protection=pin,
                                passphrase_protection=passphrase)
        self.assertEqual(res, 'random data')

    """
    def test_expected_responses(self):
        self.setup_mnemonic_pin_passphrase()

        # This is low-level test of set_expected_responses()
        # feature of debugging client

        with self.client:
            # Scenario 1 - Received unexpected message
            self.client.set_expected_responses([])
            self.assertRaises(CallException, self._some_protected_call, True, True, True)

        with self.client:
            # Scenario 2 - Received other than expected message
            self.client.set_expected_responses([proto.Success()])
            self.assertRaises(CallException, self._some_protected_call, True, True, True)

        def scenario3():
            with self.client:
                # Scenario 3 - Not received expected message
                self.client.set_expected_responses([proto.ButtonRequest(),
                                                    proto.Success(),
                                                    proto.Success()])  # This is expected, but not received
                self._some_protected_call(True, False, False)
        self.assertRaises(Exception, scenario3)

        with self.client:
            # Scenario 4 - Received what expected
            self.client.set_expected_responses([proto.ButtonRequest(),
                                                proto.PinMatrixRequest(),
                                                proto.PassphraseRequest(),
                                                proto.Success(message='random data')])
            self._some_protected_call(True, True, True)

        def scenario5():
            with self.client:
                # Scenario 5 - Failed message by field filter
                self.client.set_expected_responses([proto.ButtonRequest(),
                                                    proto.Success(message='wrong data')])
                self._some_protected_call(True, True, True)
        self.assertRaises(CallException, scenario5)
    """

    def test_no_protection(self):
        self.setup_mnemonic_nopin_nopassphrase()

        with self.client:
            self.assertEqual(self.client.debug.read_pin()[0], '')
            self.client.set_expected_responses([proto.Success()])
            self._some_protected_call(False, True, True)

    def test_pin(self):
        self.setup_mnemonic_pin_passphrase()

        with self.client:
            self.assertEqual(self.client.debug.read_pin()[0], self.pin4)
            self.client.setup_debuglink(button=True, pin_correct=True)
            self.client.set_expected_responses([proto.ButtonRequest(),
                                                proto.PinMatrixRequest(),
                                                proto.Success()])
            self._some_protected_call(True, True, False)

    def test_incorrect_pin(self):
        self.setup_mnemonic_pin_passphrase()
        self.client.setup_debuglink(button=True, pin_correct=False)
        self.assertRaises(PinException, self._some_protected_call, False, True, False)

    def test_cancelled_pin(self):
        self.setup_mnemonic_pin_passphrase()
        self.client.setup_debuglink(button=True, pin_correct=False)  # PIN cancel
        self.assertRaises(PinException, self._some_protected_call, False, True, False)

    def test_exponential_backoff_with_reboot(self):
        self.setup_mnemonic_pin_passphrase()

        self.client.setup_debuglink(button=True, pin_correct=False)

        def test_backoff(attempts, start):
            expected = 0.2 * (2 ** attempts)
            got = time.time() - start

            msg = "Pin delay expected to be at least %s seconds, got %s" % (expected, got)
            print(msg)
            self.assertLessEqual(expected, got, msg)

        for attempt in range(1, 6):
            start = time.time()
            self.assertRaises(PinException, self._some_protected_call, False, True, False)
            test_backoff(attempt, start)

if __name__ == '__main__':
    unittest.main()
