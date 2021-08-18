# Grafana-Monitor
To setup a monitor, that will provide you a lot of useful information you just need to follow this steps:
1. Install [Grafana and Node exporter with prometheus](https://github.com/CyberObiOne/node-monitoring-setup/blob/main/README.md)
2. Install  [Cosmos-IE exporter](https://github.com/CyberObiOne/Cosmos-IE/blob/master/README.md)  on server and run it
3. Install Python (if it not installed)
4. [Clone](https://github.com/CyberObiOne/Grafana-Monitor.git)
5. Edit prometheus config to include new jobs:

```
nano /etc/prometheus/prometheus.yml
  - job_name: 'cosmosie'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:26661']
  - job_name: 'osmo_price'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:8000']

```
7. Import [board config](https://github.com/CyberObiOne/Grafana-Monitor/blob/main/board.json) to Grafana
Please, be aware, that datasource can be a different
9. Run osmo_stats.py in screen or create a service for it.
```
python3 osmo_stats.py
```

