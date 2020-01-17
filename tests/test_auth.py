'''Make sure authentication is working.'''

import unittest

from server.utils import add_machine, remove_machine, authenticate # pylint: disable=E0611

class AuthTest(unittest.TestCase):
    '''Sanity checks for authentication.'''

    def setUp(self):
        # Make a tmp machine
        self.name = 'tester-mc-tesy-face'
        self.token = 'test-token-here'
        self.roles = ['client', 'target']
        add_machine(
            name=self.name, token=self.token, roles=self.roles)

    def tearDown(self):
        # Remove tmp machine
        remove_machine(self.name)

    def test_authenticate_success(self):
        '''Make sure known machine is authenticated.'''
        self.assertTrue(
            authenticate(self.name, self.token, self.roles[0]))
        self.assertTrue(
            authenticate(self.name, self.token, self.roles[1]))
        self.assertTrue(authenticate(self.name, self.token, 'any'))

    def test_authenticate_fail_unknown(self):
        '''Make sure unknown machine fails to authenticate.'''
        self.assertFalse(authenticate(
            'unknown-machine', 'nonsense', self.roles[0]))
        self.assertFalse(authenticate(
            'unknown-machine', 'nonsense', self.roles[1]))
        self.assertFalse(authenticate(
            'unknown-machine', 'nonsense', 'any'))

    def test_authenticate_fail_bad_token(self):
        '''Make sure known machine with bad token fails.'''
        self.assertFalse(
            authenticate(self.name, self.token[:-1], self.roles[0]))
        self.assertFalse(
            authenticate(self.name, self.token[:-1], self.roles[1]))
        self.assertFalse(
            authenticate(self.name, self.token[:-1], 'any'))

    def test_authenticate_fail_bad_role(self):
        '''Make sure known machine with bad role fails.'''
        self.assertFalse(
            authenticate(self.name, self.token, 'not-a-role'))

if __name__ == '__main__':
    unittest.main()
