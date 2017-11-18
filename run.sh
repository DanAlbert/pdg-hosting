#!/usr/bin/env bash
PLAYBOOK="$1"

if [[ -z $PLAYBOOK ]]; then
  echo "usage: ./run.sh PLAYBOOK"
  exit 1
fi

if [ ! -f .vault_pass ]; then
  echo >&2 ".vault_pass file not found."
  exit 1
fi

ansible-playbook -i inventory/ --vault-password-file .vault_pass "$PLAYBOOK"
