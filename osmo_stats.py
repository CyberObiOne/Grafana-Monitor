import api_calls
import random
import time
import requests
import json
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily, SummaryMetricFamily, InfoMetricFamily
from prometheus_client import start_http_server, Summary, Info
# Create a metric to track time spent and requests made.
class CustomCollector(object):     ## Class for CustomCollector which helps us  to use different metric types
        def __init__(self):
                pass
        def collect(self):
                osmo_price = api_calls.price()
                value = CounterMetricFamily("OSMO_PRICE", 'OSMO PRICE', labels='value')
                value.add_metric(["osmo_price"], osmo_price)
                yield value
                osmo_community_pool = api_calls.pool()
                value1 = CounterMetricFamily("OSMO_POOL", 'OSMO Community POOL', labels='value')
                value1.add_metric(["osmo_community_pool"], osmo_community_pool)
                yield value1
                osmo_gov_open = api_calls.gov_open_prop()
                value2 = CounterMetricFamily("OSMO_GOV_OPEN_PROPOSALS", 'OSMO GOV', labels='value')
                value2.add_metric(["osmo_gov_open"], osmo_gov_open)
                yield value2
                osmo_trx = api_calls.trx()
                value3 = GaugeMetricFamily("OSMO_TRX_COUNT", 'OSMO TRX', labels = 'value')
                value3.add_metric(["osmo_trx"], osmo_trx)
                yield value3
                osmo_gov_deposit = api_calls.gov_deposit_prop()
                value4 = GaugeMetricFamily("OSMO_GOV_DEPOST_PROPOSALS", 'OSMO GOV', labels = 'value')
                value4.add_metric(["osmo_gov_deposit"], osmo_gov_deposit)
                yield value4





if __name__ == '__main__':
        start_http_server(8000)         ## port where metrics need to be exposed.
        REGISTRY.register(CustomCollector())
        while True:
                time.sleep(10)
