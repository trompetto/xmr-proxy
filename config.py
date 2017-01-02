
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 8080

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '42jF56tc85UTZwhMQc6rHbMHTxHqK74qS2zqLyRZxLbwegsy7FJ9w4T5B69Ay5qeMEMuvVDwHNeopAxrEZkkHrMb5phovJ6'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = False
MONITORING_EMAIL = 'mail@example.com'

# Main pool
POOL_HOST = 'monerohash.com'
POOL_PORT = 3333

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'xmr-usa.dwarfpool.com'
POOL_PORT_FAILOVER = 8050

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
