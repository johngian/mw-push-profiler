import json

from decouple import config, Csv


SVC_BASE_URL = config("MW_SVC_PROF_PUSH_BASE_URL")

TOXIPROXY_ENABLED = config(
    "MW_SVC_PROF_PUSH_TOXIPROXY_ENABLED", default="False", cast=bool
)

TOXIPROXY = {
    "API_URL": config("MW_SVC_PROF_PUSH_TOXIPROXY_URL", default=""),
    "PROXIES": config(
        "MW_SVC_PROF_PUSH_TOXIPROXY_PROXIES", default="[]", cast=json.loads
    ),
    "TOXICS": config(
        "MW_SVC_PROF_PUSH_TOXIPROXY_TOXICS", default="[]", cast=json.loads
    ),
}

TOXIPROXY_ENABLED = all(TOXIPROXY.values())

MESSAGE_TYPE = "checkEchoV1"

APNS = {
    "TOKENS": config("MW_SVC_PROF_APNS_TOKENS", default="APNSTESTTOKEN", cast=Csv()),
    "DRY_RUN": config("MW_SVC_PROF_APNS_DRYRUN", default="True", cast=bool),
}

FCM = {
    "TOKENS": config("MW_SVC_PROF_FCM_TOKENS", default="FCMTESTTOKEN", cast=Csv()),
    "DRY_RUN": config("MW_SVC_PROF_FCM_DRYRUN", default="True", cast=bool),
}
