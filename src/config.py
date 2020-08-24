from decouple import config, Csv

SVC_BASE_URL = config("MW_SVC_PROF_PUSH_BASE_URL")
MESSAGE_TYPE = "checkEchoV1"

APNS = {
    "TOKENS": config("MW_SVC_PROF_APNS_TOKENS", default="APNSTESTTOKEN", cast=Csv()),
    "DRY_RUN": config("MW_SVC_PROF_APNS_DRYRUN", default="True", cast=bool),
}

FCM = {
    "TOKENS": config("MW_SVC_PROF_FCM_TOKENS", default="FCMTESTTOKEN", cast=Csv()),
    "DRY_RUN": config("MW_SVC_PROF_FCM_DRYRUN", default="True", cast=bool),
}