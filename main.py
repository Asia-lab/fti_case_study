
import solana
import json
from solana.rpc.api import Client


# Connect to testnet/devnet/main-beta cluster
# http_client = Client("https://api.devnet.solana.com")
http_client = Client("https://api.testnet.solana.com") # because it is just an case study I'm using testnet cluster
# http_client = Client("https://api.mainnet-beta.solana.com") # interactions on solana main/production blockchain

# Case study part 1 -------------------------------------------------------------------
# Validatorts count
validators_current = json.loads(http_client.get_vote_accounts().value.to_json())
validators_current_count = len(validators_current['current'])

# Validator gossip connecton details
current_gossip = json.loads(http_client.get_cluster_nodes().to_json())
current_gossip_details = current_gossip['result']

# The latest block
current_slot = http_client.get_slot().value
current_block = json.loads(http_client.get_block(current_slot).value.to_json()) 


# Case study part 2 -------------------------------------------------------------------
# Average validator count (last 30 days)
# To be able to calculate the average: 
# I'd neet to ping http cluster in following days and store somewere (database/file) the validators_current_count and some timstamp info.
print(f'Validator count (current): {validators_current_count}') # current validator count

# Average block time (last 30 days)
# At this point I've calculated only current_block_complete_time
# To be able to calculate the average: 
# I'd neet to ping http cluster in following days and store somewere (database/file) the validators_current_count and some timstamp info.
# block_time is a UNIX timestamp
current_block_timeUNIX = current_block['blockTime']
previous_slot = current_block['parentSlot']
previous_block = json.loads(http_client.get_block(previous_slot).value.to_json())
previous_block_timeUNIX = previous_block['blockTime']
# CurrentBlockCompletionTime is expressed in seconds
current_block_complete_time = current_block_timeUNIX - previous_block_timeUNIX
print(f'Block time (current): {current_block_complete_time}') # current

# IP address clusters (current)
# At this point I've got whole tpu-s stored in tpu_list... It is just an intermediary step to get list of IPs but now I am actually run out of time :(...
gossip_num = int(len(current_gossip_details))
tpu_list=[]
for i in list(range(gossip_num)):
    tpu_str = str(current_gossip_details[i]['tpu'])
    tpu_list.append(tpu_str)
# printing just a sample
print(f'Sample list of TPUs: {tpu_list[0:10]}') # printing just a sample

