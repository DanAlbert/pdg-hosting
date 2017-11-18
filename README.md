# PDG Hosting

Ansible playbooks for managing PDG servers.

## Setup

Install Python dependencies:

```bash
$ virtualenv -p python3 .env
$ . .env/bin/activate
$ pip -r requirements.txt
```

Create the `.vault_pass` file for Ansible:

```bash
$ echo "$VAULT_PASS" > .vault_pass
```

Ask a PDG admin for the vault password.

Install the GCE service account key.

```bash
$ mv path/to/key.json key.json
$ chmod 600 key.json
```

## Usage

```bash
# Recreate the infrastrucutre if it is not present. Not normally needed.
$ ./run.sh headless_clients.yaml

# Bring up the clients for pub 1.
$ ./run.sh clients_up.yaml

# Bring down the clients. Be sure to do this when they are not in use.
$ ./run.sh clients_down.yaml
```
