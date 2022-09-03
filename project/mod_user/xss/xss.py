from flask import flash

import requests

from bs4 import BeautifulSoup

from urllib.parse import parse_qsl

from time import sleep


class XSS:
    def __init__(self):
        self.session = requests.session()
        self.payloads = open('project/mod_user/xss/payloads.txt', 'r').read().splitlines()

    def get_all_forms(self, url):
        soup = BeautifulSoup(self.session.get(url).content, 'lxml')
        return soup.find_all('form')

    def get_form_details(self, form):
        details = {}

        try:
            action = form.attrs.get('action').lower()
            if action['0'] == '#':
                action = None
        except:
            action = None

        method = form.attrs.get('method', 'get').lower()

        inputs = []
        for input_tag in form.find_all(recursive=True):
            try:
                if input_tag.attrs.get('name'):
                    input_type = input_tag.attrs.get('type', 'text')
                    input_name = input_tag.attrs.get('name')
                    input_value = input_tag.attrs.get('value', '')
                    inputs.append({'type': input_type, 'name': input_name,
                                   'value': input_value})
            except:
                pass

        details['action'] = action
        details['method'] = method
        details['inputs'] = inputs

        return details

    def inject_payload(self, url, base_url, form, payload):
        details = self.get_form_details(form)

        payloads = {}
        for input in details['inputs']:
            if input['type'] == 'hidden' or input['type'] == 'submit':
                payloads[input['name']] = input['value']
            else:
                payloads[input['name']] = payload

        if not details['action']:
            details['action'] = url
        elif details['action'][0] == '/':
            details['action'] = base_url + details['action'][1:]
        elif details['action'].startswith('http'):
            details['action'] = details['action']
        else:
            details['action'] = url

        if details['method'] == 'post':
            result = self.session.post(details['action'], data=payloads)
        else:
            result = self.session.get(details['action'], params=payloads)

        return str(result.text).lower()

    def has_error(self, result, text):
        if text in result:
            return True
        return False

    def parse_qs(self, qs):
        return dict(parse_qsl(qs))

    def login(self, login_url, login_params, form_number, response_text):
        forms = self.get_all_forms(login_url)

        if len(forms) < form_number:
            flash(
                f'Can not find login form number {form_number} .', category='danger')
            return False

        form = forms[form_number-1]

        details = self.get_form_details(form)

        payloads = self.parse_qs(login_params)

        for input in details['inputs']:
            if input['type'] == 'hidden':
                payloads[input['name']] = input['value']

        try:
            if details['method'] == 'post':
                result = self.session.post(login_url, data=payloads)
            else:
                result = self.session.get(login_url, params=payloads)
        except Exception as e:
            flash('Something wrong in login the page .', category='danger')
            return False

        if response_text.lower() in str(result.text).lower():
            flash('Logined successfully .', category='success')
            return True

        flash(
            f'Can not find text \"{response_text}\" in login response .', category='danger')
        return False

    def run(self, url, base_url):
        error_forms = []
        forms = self.get_all_forms(url)

        for index, form in enumerate(forms):
            for payload in self.payloads:
                script = self.inject_payload(url, base_url, form, payload)
                if self.has_error(script, payload):
                    error_forms.append((index+1, payload))
                    break

        if not error_forms:
            flash('No errors found .', category='danger')
        else:
            flash('Some errors found .', category='success')

        return error_forms
