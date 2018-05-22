#!/usr/bin/env python3

import json

def load_auth_config(filename="config_auth.json"):
    config = {}
    with open(filename) as f:
        config = json.load(f)
    return config

def main():
    pass

if __name__ == "__main__":
    main()

