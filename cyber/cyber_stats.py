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
                cyber_price = api_calls.price()
                value = CounterMetricFamily("Cyber_PRICE", 'Cyber PRICE', labels='value')
                value.add_metric(["cyber_price"], cyber_price)
                yield value
                cyber_community_pool = api_calls.pool()
                value1 = CounterMetricFamily("Cyber_POOL", 'Cyber Community POOL', labels='value')
                value1.add_metric(["cyber_community_pool"], cyber_community_pool)
                yield value1
                cyber_gov_open = api_calls.gov_open_prop()
                value2 = CounterMetricFamily("Cyber_GOV_OPEN_PROPOSALS", 'Cyber GOV', labels='value')
                value2.add_metric(["cyber_gov_open"], cyber_gov_open)
                yield value2
                cyber_gov_deposit = api_calls.gov_deposit_prop()
                value3 = GaugeMetricFamily("Cyber_GOV_DEPOST_PROPOSALS", 'Cyber GOV', labels = 'value')
                value3.add_metric(["cyber_gov_deposit"], cyber_gov_deposit)
                yield value3
                cyber_bonded_tokens = api_calls.bonded_tokens()
                value4 = GaugeMetricFamily("Cyber_BONDED_TOKEN", 'Cyber TOKEN ', labels = 'value')
                value4.add_metric(["cyber_bonded_tokens"], cyber_bonded_tokens)
                yield value4
                cyber_unbonded_tokens = api_calls.unbonded_tokens()
                value5 = GaugeMetricFamily("Cyber_UNBONDED_TOKEN", 'Cyber TOKEN ', labels = 'value')
                value5.add_metric(["cyber_unbonded_tokens"], cyber_unbonded_tokens)
                yield value5
                cyber_inflation = api_calls.inflation()
                value6 = GaugeMetricFamily("Cyber_INFLATION", 'Cyber INFLATION ', labels = 'value')
                value6.add_metric(["cyber_inflation"], cyber_inflation)
                yield value6
                cyber_status = api_calls.status()
                value7 = GaugeMetricFamily("Cyber_VALIDATOR_STATUS", 'Cyber VALIDATOR STATUS ', labels = 'value')
                value7.add_metric(["cyber_status"], cyber_status)
                yield value7
                cyber_commission = api_calls.commission()
                value8 = GaugeMetricFamily("Cyber_VALIDATOR_COMMISSION", 'Cyber VALIDATOR COMMISSION ', labels = 'value')
                value8.add_metric(["cyber_commission"], cyber_commission)
                yield value8
                cyber_pre_commits = api_calls.pre_commits()
                value9 = GaugeMetricFamily("Cyber_VADATOR_PRE_COMMITS", 'Cyber VALIDATOR PRE COMMITS ', labels = 'value')
                value9.add_metric(["cyber_pre_commits"], cyber_pre_commits)
                yield value9
                cyber_rewards = api_calls.delegations()
                value10 = GaugeMetricFamily("Cyber_VADATOR_STAKED", 'Cyber VALIDATOR STAKED ', labels = 'value')
                value10.add_metric(["cyber_rewards"], cyber_rewards)
                yield value10
                cyber_reward_balance = api_calls.reward_balance()
                value11 = GaugeMetricFamily("Cyber_VADATOR_REWARDS", 'Cyber VALIDATOR REWARDS ', labels = 'value')
                value11.add_metric(["cyber_reward_balance"], cyber_reward_balance)
                yield value11
                cyber_links = api_calls.links()
                value11 = GaugeMetricFamily("Cyber_GRAPH_LINKS", 'Cyber GRAPH LINKS ', labels = 'value')
                value11.add_metric(["cyber_links"], cyber_links)
                yield value11

if __name__ == '__main__':
        start_http_server(8000)         ## port where metrics need to be exposed.
        REGISTRY.register(CustomCollector())
        while True:
                time.sleep(10)
