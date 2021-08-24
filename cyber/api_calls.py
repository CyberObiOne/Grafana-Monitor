import requests
import json

def pool():
   pool = requests.get('https://lcd.bostromdev.cybernode.ai/cosmos/distribution/v1beta1/community_pool')
   community_pool = pool.json()["pool"][0]["amount"]
   return (community_pool)

def trx():
   trx = requests.get('https://api-osmosis.cosmostation.io/v1/status')
   trx_count = trx.json()["total_txs_num"]
   return (trx_count)

def gov_open_prop():
   gov = requests.get('https://lcd.bostromdev.cybernode.ai/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   open_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_VOTING_PERIOD":
                  open_count = open_count + 1

   return (open_count)

def gov_deposit_prop():
   gov = requests.get('https://lcd.bostromdev.cybernode.ai/cosmos/gov/v1beta1/proposals')
   data = gov.json()["proposals"]
   deposit_count = 0
   for i in data:
           if  i["status"] == "PROPOSAL_STATUS_DEPOSIT_PERIOD":
                  deposit_count = deposit_count + 1
   return (deposit_count)

def price():
   price = requests.get('https://market-data.cybernode.ai/api/coins/cyb')
   data = price.json()['market_data']['current_price']['usd']
   return (data)

def bonded_tokens():
   tokens = requests.get('https://lcd.bostromdev.cybernode.ai/staking/pool')
   bonded_tokens = tokens.json()['result']['bonded_tokens']
   return (bonded_tokens)

def unbonded_tokens():
   tokens = requests.get('https://lcd.bostromdev.cybernode.ai/staking/pool')
   unbonded_tokens = tokens.json()['result']['not_bonded_tokens']
   return (unbonded_tokens)

def inflation():
   inflation = requests.get('https://lcd.bostromdev.cybernode.ai/minting/inflation')
   inflation_total = inflation.json()['result']
   return (inflation_total)

def status():
   validator = requests.get('https://lcd.bostromdev.cybernode.ai/cosmos/staking/v1beta1/validators/bostromvaloper1ke7kxdn29w2lrxt9dzusa6shvmwd8xm9suu4j2')
   data = validator.json()['validator']['jailed']
   return (data)
