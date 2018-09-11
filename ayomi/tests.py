from django.test import TestCase
from django.contrib.auth.models import User

import json

class TestCalls(TestCase):
    def setUp(self):
        self.username = "test"
        self.password = "password"
        self.user = User.objects.create(username=self.username, password=self.password)
    
    def test_call_view_denies_anonymous(self):
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/')
        response = self.client.post('/main/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/main/')

    def test_call_apis_denies_anontmous(self):
        response = self.client.get('/change_email/test@test.com/', follow=True)
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/change_first_name/test1/', follow=True)
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/change_last_name/test2', follow=True)
        self.assertEqual(response.status_code, 404)
        
    def test_call_view_allow(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/main/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_call_apis_denies_anontmous(self):
        response = self.client.get('/change_email/test@test.com/', follow=True)
        self.assertEqual(response.status_code, 200)
        re = json.reads(self.response.content)
        self.assertEqual(re.state, True)
        self.assertEqual(re.email, "test@test.com")

        #response = self.client.get('/change_first_name/test@test.com/', follow=True)
        #self.assertEqual(response.status_code, 200)

        #response = self.client.get('/change_last_name/test@test.com/', follow=True)
        #self.assertEqual(response.status_code, 200)
