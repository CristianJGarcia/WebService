#!/usr/bin/env python3
import unittest
import requests


class TestAPI(unittest.TestCase):
    def test0_hello(self):
        resp = requests.get("http://52.170.167.62:12075/hello")
        self.assertEqual(resp.json(), {'message': 'hello yourself'})

    def test0_properties(self):

        resp = requests.get("http://52.170.167.62:12075/properties")
        self.assertEqual(resp.status_code, 200)

    def test1_properties_add(self):

        headers = {'Content-Type': 'application/json',
                   'Authorization': 'cs4783FTW'}
        payload = {"address": "1015 W 4th st", "city": "weslaco",
                   "id": -1, "state": "TX", "zip": "78596"}
        resp = requests.post(
            "http://52.170.167.62:12075/properties", json=payload, headers=headers)
        self.assertEqual(resp.status_code, 200)

    def test2_properties_view_by_id(self):

        pID = requests.get(
            "http://52.170.167.62:12075/properties").json()[-1]['id']

        resp = requests.get(
            f"http://52.170.167.62:12075/properties/{pID}")

        self.assertEqual(resp.status_code, 200)

    def test3_properties_update_by_id(self):

        headers = {'Content-Type': 'application/json',
                   'Authorization': 'cs4783FTW'}
        payload = {"address": "testing", "city": "test",
                   "id": -1, "state": "CA", "zip": "test"}
        pID = requests.get(
            "http://52.170.167.62:12075/properties").json()[-1]['id']

        resp = requests.put(
            f"http://52.170.167.62:12075/properties/{pID}", json=payload, headers=headers)

        self.assertEqual(resp.status_code, 200)

    def test4_properties_delete_by_id(self):
        print(10)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'cs4783FTW'}
        pID = requests.get(
            "http://52.170.167.62:12075/properties").json()[-1]['id']

        resp = requests.delete(
            f"http://52.170.167.62:12075/properties/{pID}", headers=headers)

        self.assertEqual(resp.status_code, 200)


"""
    def test5_properties_HTTPS(self):
        print(5)
        resp = requests.get(
            "https://52.170.167.62:12070/properties", verify=False)
        self.assertEqual(resp.status_code, 200)

    def test6_properties_add_HTTPS(self):
        print(6)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'cs4783FTW'}
        payload = {"address": "1015 W 4th st", "city": "weslaco",
                   "id": -1, "state": "TX", "zip": "78596"}
        resp = requests.post(
            "https://52.170.167.62:12070/properties", json=payload, headers=headers, verify=False)
        self.assertEqual(resp.status_code, 200)

    def test7_properties_view_by_id_HTTPS(self):
        print(7)
        pID = requests.get(
            "https://52.170.167.62:120700/properties", verify=False).json()[-1]['id']
        print(pID)
        resp = requests.get(
            f"https://cs47832.fulgentcorp.com:12070/properties/{pID}", verify=False)

        self.assertEqual(resp.status_code, 200)

    def test8_properties_update_by_id_HTTPS(self):
        print(8)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'cs4783FTW'}
        payload = {"address": "testing", "city": "test",
                   "id": -1, "state": "CA", "zip": "test"}
        pID = requests.get(
            "https://cs47832.fulgentcorp.com:12070/properties", verify=False).json()[-1]['id']
        print(pID)
        resp = requests.put(
            f"https://cs47832.fulgentcorp.com:12070/properties/{pID}", verify=False, json=payload, headers=headers)

        self.assertEqual(resp.status_code, 200)

    def test9_properties_delete_by_id_HTTPS(self):
        print(9)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'cs4783FTW'}
        pID = requests.get(
            "https://cs47832.fulgentcorp.com:12070/properties", verify=False).json()[-1]['id']
        print(pID)

        resp = requests.delete(
            f"https://cs47832.fulgentcorp.com:12070/properties/{pID}", verify=False, headers=headers)

        self.assertEqual(resp.status_code, 200)
"""

if __name__ == '__main__':
    unittest.main()
