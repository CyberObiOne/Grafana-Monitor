import requests
import json

def pool():
   pool = requests.get('http://node_IP:1317/cosmos/distribution/v1beta1/community_pool')
   community_pool = pool.json()["pool"][0]["amount"]
   return (community_pool)

def trx():
   trx = requests.get('https://api-osmosis.cosmostation.io/v1/status')
   trx_count = trx.json()["total_txs_num"]
   return (trx_count)

def gov_open_prop():
   gov = requests.get('http://node_IP:1317/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   open_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_VOTING_PERIOD":
                  open_count = open_count + 1

   return (open_count)

def gov_deposit_prop():
   gov = requests.get('http://node_IP:1317/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   deposit_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_DEPOSIT_PERIOD":
                  deposit_count = deposit_count + 1
   return (deposit_count)

def price():
   while True:
      price = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=osmosis&vs_currencies=usd")
      osmo_price = price.json()['osmosis']['usd']
      return (osmo_price)
