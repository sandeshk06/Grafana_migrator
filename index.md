# Grafana_migrator
Used for migrating Dashboards and  Datasources form one Grafana Instance to another Grafana Instance

**What is Grafana ?**

Grafana is a multi-platform open source analytics and interactive visualization web application. It provides charts, graphs, and alerts for the web when connected to supported data sources.

**What is Grafana Migrator Tool**

- Based on wizzy grafana backup tool
- Python based Grafana migration tool for migrating datasources and  dashboards form one grafana instance to  another grafana instance.
- Useful when we need to migrate grafana old instance to new instance.

**How to use**
- Install Wizzy **https://grafana-wizzy.com**
- Configure Grafana Source Url
- Import datasources and  Dashboard
- Configure Grafana Destination Url
- Export datasources and  Dashboard

**Prerequisite:**
- python3,pip3,git, wizzy installed on system
- pip3 install bcolors

**Steps to Run:**
- git clone https://github.com/sandeshk06/grafana_migrator .git
- cd grafana_migrator
- python3 grafana_migration.py

**Using Dockerfile:**
- git clone https://github.com/sandeshk06/grafana_migrator .git
- cd grafana_migrator
- docker build -t grafana_migrator .
- docker run -it --name grafana_migration -e PYTHONIOENCODING=utf-8 grafana_migrtor
