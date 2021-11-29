import requests
import json


class Network:

    @property
    def query_route(self):
        return f"{self.env['host_url']}:{self.env['query_port']}"

    @property
    def submit_route(self):
        return f"{self.env['host_url']}:{self.env['submission_port']}"

    @property
    def ledger_route(self):
        return f"{self.env['host_url']}:{self.env['ledger_port']}"

    @property
    def explorer_route(self):
        return f"{self.env['host_url']}:{self.env['explorer_api_port']}"

    def __init__(self, env):
        """
        :param  env:dictionary sdk session environment
        """
        self.env = env

    def api_post(self, url, data, config):
        """
        :param  url:str
        :param  data:{}
        :param  config:{
            headers,
            params
        }
        """
        # TODO: check params and headers
        response = requests.post(url,
                                 data=json.dumps(data),
                                 params=config["params"],
                                 headers=config["headers"])
        # TODO: return

    def get_owned_sids(self, address: str, config: dict):
        """
        :param  address:str     utf-8 encoded
        :param  config:dict{
            headers,
            params
        }
        """
        address = address.decode("utf-8")
        url = f"{self.query_route}/get_owned_utxos/{address}"
        print(f"Query URL: {url}")
        response = requests.get(url,
                                params=config.get("params", None),
                                headers=config.get("headers", None))
        if response.status_code != 200:
            print(f"Getting owned sids from {response.url} failed")

        return response.text

    def get_related_sids(self, address, config):
        """
        :param  address:str     utf-8 encoded
        :param  config:{
            headers,
            params
        }
        """
        address = address.decode("utf-8")
        url = f"{self.query_route}/get_related_txns/{address}"
        response = requests.get(url,
                                params=config["params"],
                                headers=config["headers"])

        return response

    def get_utxo(self, utxo_sid, config):
        """
        :param  utxo_sid:int
        :param  config:{
            headers,
            params
        }
        """
        url = f"{self.ledger_route}/utxo_sid/{utxo_sid}"
        response = requests.get(url,
                                params=config["params"],
                                headers=config["headers"])
        print(response)

    def get_owner_memo(self, utxo_sid, config):
        """
        :param  utxo_sid:int
        :param  config:{
            headers,
            params
        }
        """
        url = f"{self.ledger_route}/get_owner_memo/{utxo_sid}"
        response = requests.get(url,
                                params=config["params"],
                                headers=config["headers"])
        print(response)
