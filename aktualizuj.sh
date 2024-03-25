#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

set -o pipefail
set -e

function upload() (
    set -x
    scp * root@10.0.0.7:/projekt/
    scp .env root@10.0.0.7:/projekt/
)

function install() (
    ssh root@10.0.0.7 << EOF
    set -ex
    cd /projekt
    uv --version || pip install --upgrade uv
    ls .venv > /dev/null || uv venv
    uv pip install -r requirements.txt
EOF
)

function update_crontab() (
    set -x
    ssh root@10.0.0.7 "cd /projekt && crontab rozklad_monitoru"
)

function run() (
    cd $SCRIPT_DIR
    source .venv/bin/activate
    source .env
    python monitor.py
)

function plot() (
    cd $SCRIPT_DIR
    source .venv/bin/activate
    source .env
    python wykres.py
)

function help() {
    echo "Usage: $0 [instaluj|zaladuj|uruchom|wykres|crontab]"
}

for var in "$@"
do
    case $var in
        zaladuj)
            upload
            ;;
        instaluj)
            install
            ;;
        uruchom)
            run
            ;;
        wykres)
            plot
            ;;
        crontab)
            update_crontab
            ;;
        *)
            help
            ;;
    esac
done
