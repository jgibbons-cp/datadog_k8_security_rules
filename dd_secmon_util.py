import getopt
import json
import os
import requests
from shutil import copyfile
import sys

FIRST_ARG = 1
DEBUG = True
FAIL = -1

api_key = os.environ["DD_API_KEY"]
app_key = os.environ["DD_APP_KEY"]

headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

def list_sec_rules():
    """Return an org's security rules."""

    url = "https://api.datadoghq.com/api/v2/security_monitoring/rules?page[size]=500"
    sec_rules = \
        requests.get(url, headers=headers)

    sec_rules = sec_rules.json()

    return sec_rules


def get_sec_rule_name(name):
    """Get the security rule from the org that matches the rule name."""

    all_rules = list_sec_rules()
    mode = "w"

    for rule in all_rules["data"]:

        if rule["name"] == name:
            formatted_json = json.dumps(rule, indent=4)
            formatted_rule_name = name.replace(" ", "_")
            formatted_rule_name = formatted_rule_name + ".yaml"
            f = open(formatted_rule_name, mode)
            f.write(formatted_json)
            f.close()
            break

    if rule["name"] != name:
        print("No rules match that rule name... Later gator...\n")
        sys.exit(FAIL)


def add_sec_rule(name):
    """Add a security rule that matches name from JSON pulled using get_sec_rule_name(name)."""
    orig_rule_name = name
    rule_name = orig_rule_name.replace(".yaml", "_tmp.yaml")

    try:
        copyfile(orig_rule_name, rule_name)
        with open(rule_name) as f:
            json_data = json.load(f)
    except FileNotFoundError as e:
        exception_string = str(e)
        print("Error: " + exception_string + "... exiting...\n")
        sys.exit(FAIL)

    try:
        json_data.pop('creationAuthorId')
        json_data.pop('hasExtendedTitle')
        json_data.pop('type')
        json_data.pop('id')
        json_data.pop('version')
        json_data.pop('createdAt')
        json_data.pop('isDefault')
        json_data.pop('no')
    except Exception:
        pass

    url = "https://api.datadoghq.com/api/v2/security_monitoring/rules"
    sec_rules = \
        requests.post(url, headers=headers, json=json_data)

    f.close()
    os.remove(rule_name)

def main():
    argv = sys.argv[FIRST_ARG:]

    """-l list rules for an org, -g get a rule by name from an org, -a add a rule to another account"""
    try:
        opts, args = getopt.getopt(argv, "lg:a:")
    except getopt.GetoptError as e:
        print("Argument error: " + str(e) + ".  Exiting... Later gator...\n")
        sys.exit(FAIL)

    for opt, arg in opts:
        if opt in ['-l']:
            security_rules = list_sec_rules()

            if DEBUG is True:
                print(security_rules)
        elif opt in ['-g']:
            rule_name = arg
            get_sec_rule_name(rule_name)
        elif opt in ['-a']:
            rule_name = arg
            add_sec_rule(rule_name)


if __name__ == "__main__":
    main()