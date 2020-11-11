import getopt
import json
import os
import requests
import sys

FIRST_ARG = 1
DEBUG = False
FAIL = -1

api_key = os.environ["DD_API_KEY"]
app_key = os.environ["DD_APP_KEY"]


def list_sec_rules():
    """Return an org's security rules."""

    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    url = "https://api.datadoghq.com/api/v2/security_monitoring/rules?page[size]=500"
    sec_rules = \
        requests.get(url, headers=headers)

    sec_rules = sec_rules.json()

    return sec_rules


def get_sec_rule_name(name):
    """Get the security rule from teh org that matches name."""

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


argv = sys.argv[FIRST_ARG:]

"""-l list rules for an org, -g get a rule by name from an org"""
try:
    opts, args = getopt.getopt(argv, "lg:")
except getopt.GetoptError as e:
    print("Argument error: " + str(e) + ".  Exiting... Later gator...\n")
    sys.exit(FAIL)

for opt, arg in opts:
    if opt in ['-l']:
        security_rules = list_sec_rules()

        sys.exit()

        if DEBUG is True:
            print(security_rules)
    elif opt in ['-g']:
        rule_name = arg
        get_sec_rule_name(rule_name)
