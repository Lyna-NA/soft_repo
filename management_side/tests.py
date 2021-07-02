# from django.test import TestCase,override_settings
# from django.contrib.auth.models import Permission, User
# from django.contrib.auth import (
#     BACKEND_SESSION_KEY, REDIRECT_FIELD_NAME, SESSION_KEY,
# )
# import itertools
# from django.urls import NoReverseMatch, reverse


# class AuthViewsTestCase(TestCase):
#     """
#     Helper base class for all the follow test cases.
#     """

#     @classmethod
#     def setUpTestData(cls):
#         cls.u1 = User.objects.create_user(username='testclient', password='password', email='testclient@example.com')
#         cls.u3 = User.objects.create_user(username='staff', password='password', email='staffmember@example.com')

#     def login(self, username='testclient', password='password', url='/login/'):
#         response = self.client.post(url, {
#             'username': username,
#             'password': password,
#         })
#         self.assertIn(SESSION_KEY, self.client.session)
#         return response

#     def logout(self):
#         response = self.client.get('/admin/logout/')
#         self.assertEqual(response.status_code, 200)
#         self.assertNotIn(SESSION_KEY, self.client.session)

#     def assertFormError(self, response, error):
#         """Assert that error is found in response.context['form'] errors"""
#         form_errors = list(itertools.chain(*response.context['form'].errors.values()))
#         self.assertIn(str(error), form_errors)


# @override_settings(ROOT_URLCONF='django.contrib.auth.urls')
# class AuthViewNamedURLTests(AuthViewsTestCase):

#     def test_named_urls(self):
#         "Named URLs should be reversible"
#         expected_named_urls = [
#             ('login', [], {}),
#             ('logout', [], {}),
#             ('password_change', [], {}),
#             ('password_change_done', [], {}),
#             ('password_reset', [], {}),
#             ('password_reset_done', [], {}),
#             ('password_reset_confirm', [], {
#                 'uidb64': 'aaaaaaa',
#                 'token': '1111-aaaaa',
#             }),
#             ('password_reset_complete', [], {}),
#         ]
#         for name, args, kwargs in expected_named_urls:
#             with self.subTest(name=name):
#                 try:
#                     reverse(name, args=args, kwargs=kwargs)
#                 except NoReverseMatch:
#                     self.fail("Reversal of url named '%s' failed with NoReverseMatch" % name)

