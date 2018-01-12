# coin_market_cap_api
Python wrapper around the coinmarketcap.com api

```python

#Creating an instance of the API
api = cmc_api.Coin_Market_API()


#A list of currency's that results can be converted to
api.currency_list
'''
PRINT OUTPUT
['AUD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 
'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK',
'NZD', 'PHP', 'PKR', 'PLN', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'ZAR']
'''


#A list of fields returned from coin data requests
api.coin_fields
'''
['id', 'name', 'symbol', 'rank', 'price_usd', 'price_btc', '24h_volume_usd',
'market_cap_usd', 'available_supply', 'total_supply', 'max_supply',
'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated']
'''


#A list of feilds returned from market data requests
api.market_fields
'''
['total_market_cap_usd', 'total_24h_volume_usd', 'bitcoin_percentage_of_market_cap',
'active_currencies', 'active_assets', 'active_markets', 'last_updated']
'''


#Get a current list of the top 100 tickers. To get a list of all tickers set limit=0
#coin_ids = api.get_coin_id(start=0, limit=100)
'''
PRINT OUTPUT: A list of 100 coin id's. the size of the output can be adjusted by setting limit to a differnt int.
['bitcoin', 'ethereum', 'ripple', 'bitcoin-cash', 'cardano', 
'litecoin', 'nem', 'iota', 'stellar', 'dash', 'neo', 'tron', 'monero', 
'eos', 'icon', 'bitcoin-gold', 'qtum', 'ethereum-classic', 'raiblocks', 'lisk', 
'verge', 'omisego', 'bytecoin-bcn', 'zcash', 'bitconnect', 'siacoin', 'populous', 
'stratis', 'binance-coin', 'dentacoin', 'bitshares', 'ardor', 'kucoin-shares', 'tether', 
'dogecoin', 'status', 'steem', 'waves', 'vechain', 'dragonchain', 'wax', 'veritaseum', 
'digibyte', 'ark', 'hshare', '0x', 'augur', 'dent', 'komodo', 'golem-network-tokens', 
'basic-attention-token', 'electroneum', 'salt', 'decred', 'kyber-network', 'medibloc', 
'pivx', 'funfair', 'qash', 'experience-points', 'ethos', 'kin', 'neblio', 'substratum', 
'aion', 'nexus', 'factom', 'reddcoin', 'power-ledger', 'enigma-project', 'bytom', 'aeternity',
'zclassic', 'request-network', 'aelf', 'iconomi', 'bitcoindark', 'gas', 'deepbrain-chain',
'digixdao', 'cobinhood', 'maidsafecoin', 'monacoin', 'byteball', 'nxt', 'storm', 'rchain', 
'walton', 'syscoin', 'gnosis-gno', 'bancor', 'raiden-network-token', 'achain', 'santiment', 
'chainlink', 'digitalnote', 'quantstamp', 'gamecredits', 'zcoin', 'blockv']
'''


#Get current data for a specific ticker
#coin_data = api.get_single_coin_data(coin_list[2]) #ripple
'''
PRINT OUTPUT: A list containing one dictionary.
[{'id': 'ripple', 'name': 'Ripple', 'symbol': 'XRP', 
'rank': '3', 'price_usd': '1.90375', 'price_btc': '0.00013334', 
'24h_volume_usd': '3888060000.0', 'market_cap_usd': '73749643126.0', 
'available_supply': '38739142811.0', 'total_supply': '99993093880.0', 
'max_supply': '100000000000', 'percent_change_1h': '-5.29', 'percent_change_24h': '-21.03', 
'percent_change_7d': '-27.32', 'last_updated': '1515562440'}]
'''


#Get current data for a specific ticker with default datestring instead of a unix timestamp by
#passing unix_timestamp = False to the given function.
#coin_data = api.get_single_coin_data(coin_list[2], unix_timestamp = False) #ripple
'''
[{'id': 'ripple', 'name': 'Ripple', 'symbol': 'XRP',
'rank': '3', 'price_usd': '1.89746', 'price_btc': '0.00013302',
'24h_volume_usd': '3891700000.0', 'market_cap_usd': '73505973918.0',
'available_supply': '38739142811.0', 'total_supply': '99993093880.0',
'max_supply': '100000000000', 'percent_change_1h': '-5.37', 'percent_change_24h': '-21.21',
'percent_change_7d': '-27.62', 'last_updated': '01/10/2018 12:39:05 AM'}]
'''

#Get current data for a specific ticker with custom datestring instead of a unix timestamp by 
#passing timestamp_format and setting it equal to an appropriate datetime formate code. 
#coin_data = api.get_single_coin_data(coin_list[2], timestamp_format='%Y %I:%M %p') #ripple
'''
PRINT OUTPUT: A list containing one dictionary. Note that the 'last_updated' field is a date string
[{'id': 'ripple', 'name': 'Ripple', 'symbol': 'XRP',
'rank': '3', 'price_usd': '1.89746', 'price_btc': '0.00013302',
'24h_volume_usd': '3891700000.0', 'market_cap_usd': '73505973918.0',
'available_supply': '38739142811.0', 'total_supply': '99993093880.0',
'max_supply': '100000000000', 'percent_change_1h': '-5.37', 'percent_change_24h': '-21.21',
'percent_change_7d': '-27.62', 'last_updated': '2018 12:39 AM'}]
'''


#Get current data for a specific ticker while excluding feilds that you arent interest in
# exclude = ['percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated']
# coin_data = api.get_single_coin_data(coin_list[2], excluded_fields=exclude) #ripple
'''
PRINT OUTPUT: A list containing a dictionary, which does not include the items specified in exclude
[{'id': 'ripple', 'name': 'Ripple', 'symbol': 'XRP', 
'rank': '3', 'price_usd': '1.92182', 'price_btc': '0.00013334', 
'24h_volume_usd': '3953010000.0', 'market_cap_usd': '74449659437.0', 
'available_supply': '38739142811.0', 'total_supply': '99993093880.0', 
'max_supply': '100000000000'}]
'''


#Get current data for a specific ticker while only including feilds that you are interest in
# include = ['id', 'name', 'symbol', 'rank', 'available_supply', 'total_supply',]
# coin_data = api.get_single_coin_data(coin_list[2], include_only=include) #ripple
'''
[{'id': 'ripple', 'name': 'Ripple', 'symbol': 'XRP', 
'rank': '3', 'available_supply': '38739142811.0', 'total_supply': '99993093880.0'}]
'''


#Get current data for more than one coin 
#bulck_data = api.get_bulck_coin_data(limit=2)
'''
PRINT OUTPUT: A list containing data on the top 2 coins
[{'id': 'bitcoin', 'name': 'Bitcoin', 'symbol': 'BTC', 'rank': '1', 'price_usd': '14413.5',
'price_btc': '1.0', '24h_volume_usd': '16973700000.0', 'market_cap_usd': '242048427862',
'available_supply': '16793175.0', 'total_supply': '16793175.0', 'max_supply': '21000000.0',
'percent_change_1h': '-0.09', 'percent_change_24h': '-5.71', 'percent_change_7d': '-5.25', 'last_updated': '1515563361'}, 

{'id': 'ethereum', 'name': 'Ethereum', 'symbol': 'ETH', 'rank': '2', 'price_usd': '1369.78', 
'price_btc': '0.0957777', '24h_volume_usd': '9317090000.0', 'market_cap_usd': '132709776049', 
'available_supply': '96884008.0', 'total_supply': '96884008.0', 'max_supply': None, 
'percent_change_1h': '-2.3', 'percent_change_24h': '13.13', 'percent_change_7d': '53.87', 'last_updated': '1515563349'}]
'''


#when requesting data for more than one coin, custom time format can be applied by
#passing timestamp_format and setting it equal to an appropriate datetime formate code
#passing unix_timestamp = False will result in the default date fromat string.
#bulck_data = api.get_bulck_coin_data(limit=2, timestamp_format='%Y %I:%M %p')
'''
PRINT OUTPUT: A list containing data on multiple coins where 'last_updated' is a date string
[{'id': 'bitcoin', 'name': 'Bitcoin', 'symbol': 'BTC', 'rank': '1', 'price_usd': '14337.6',
'price_btc': '1.0', '24h_volume_usd': '16971600000.0', 'market_cap_usd': '240773825880',
'available_supply': '16793175.0', 'total_supply': '16793175.0', 'max_supply': '21000000.0', 
'percent_change_1h': '-0.76', 'percent_change_24h': '-6.17', 'percent_change_7d': '-5.76', 'last_updated': '2018 12:54 AM'}, 

{'id': 'ethereum', 'name': 'Ethereum', 'symbol': 'ETH', 'rank': '2', 'price_usd': '1364.46', 
'price_btc': '0.0954646', '24h_volume_usd': '9275140000.0', 'market_cap_usd': '132194353128', 
'available_supply': '96884008.0', 'total_supply': '96884008.0', 'max_supply': None, 
'percent_change_1h': '-2.83', 'percent_change_24h': '12.7', 'percent_change_7d': '53.27', 'last_updated': '2018 12:54 AM'}]
'''


#specific coin id's can also be passed as *args when requesting data for more than one coin: coin_list[7]='iota' coin_list[15]='bitcoin-gold'
#bulck_data = api.get_bulck_coin_data(coin_list[7], coin_list[15])
'''
PRINT OUTPUT:
[{'id': 'iota', 'name': 'IOTA', 'symbol': 'MIOTA', 'rank': '8', 'price_usd': '3.48527',
'price_btc': '0.00024255', '24h_volume_usd': '196746000.0', 'market_cap_usd': '9687413509.0',
'available_supply': '2779530283.0', 'total_supply': '2779530283.0', 'max_supply': '2779530283.0',
'percent_change_1h': '-0.5', 'percent_change_24h': '-9.21', 'percent_change_7d': '-13.23', 'last_updated': '1515564850'},

{'id': 'bitcoin-gold', 'name': 'Bitcoin Gold', 'symbol': 'BTG', 'rank': '16', 'price_usd': '236.833',
'price_btc': '0.0164818', '24h_volume_usd': '150892000.0', 'market_cap_usd': '3968231314.0', 
'available_supply': '16755399.0', 'total_supply': '16855399.0', 'max_supply': '21000000.0',
'percent_change_1h': '-0.76','percent_change_24h': '-2.05', 'percent_change_7d': '-14.05', 'last_updated': '1515564856'}]
'''


#Note: the coin id's you're searching for have to be within the limit of your request otherwise an empty list will be returned.
#In the previous example the default limit of 100 ensures that coin_list[7] and coin_list[15] are included in the results
#bulck_data = api.get_bulck_coin_data(coin_list[7], coin_list[8],limit=5,)
'''
PRINT OUTPUT: []
'''


#A list of fields to exclude can also be specified when requesting data on more than one coin.
# exclude = ['rank', 'max_supply', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated']
# bulck_data = api.get_bulck_coin_data(coin_list[7], coin_list[15], excluded_fields=exclude)
'''
PRINT OUTPUT: A list of multiple coins which does not include fields specified in exclude
[[{'id': 'iota', 'name': 'IOTA', 'symbol': 'MIOTA', 'price_usd': '3.49379', 
'price_btc': '0.00024323', '24h_volume_usd': '196636000.0', 'market_cap_usd': '9711095107.0', 
'available_supply': '2779530283.0', 'total_supply': '2779530283.0'}, 

{'id': 'bitcoin-gold', 'name': 'Bitcoin Gold', 'symbol': 'BTG', 'price_usd': '235.755', 
'price_btc': '0.0164127', '24h_volume_usd': '148037000.0', 'market_cap_usd': '3950171941.0', 
'available_supply': '16755411.0', 'total_supply': '16855411.0'}]
'''


#A list of fields to include can be passed to ensure only those feilds are returned for each coin
#by passing include_only and a list of values
# include = ['id', 'name', 'symbol', 'price_usd', 'last_updated']
# bulck_data = api.get_bulck_coin_data(coin_list[7], coin_list[15], include_only=include, unix_timestamp=False)
'''
PRINT OUTPUT: NOTE that other **kwargs can be combined
[{'id': 'iota', 'name': 'IOTA', 'symbol': 'MIOTA', 
'price_usd': '3.71713', 'last_updated': '01/10/2018 01:54:12 PM'}, 

{'id': 'bitcoin-gold', 'name': 'Bitcoin Gold', 'symbol': 'BTG', 
'price_usd': '236.525', 'last_updated': '01/10/2018 01:54:16 PM'}]
'''

```
