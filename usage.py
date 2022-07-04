from settings.config_classes import Config

if __name__ == "__main__":

    con_QA = Config("QA")
    print("QA stage")
    print("********")
    print(con_QA.psguser)
    print(con_QA.psghost)
    print(con_QA.pushiOS_url)
    print(con_QA.pushiOSapi_key)
    print("")

    con_PRED = Config("PRED")
    print("PRED stage")
    print("**********")
    print(con_PRED.psguser)
    print(con_PRED.psghost)
    print(con_PRED.pushiOS_url)
    print(con_PRED.pushiOSapi_key)
    print("")

    con_generic = Config()
    print("stage from yaml")
    print("***************")
    print(con_generic.psguser)
    print(con_generic.psghost)
    print(con_generic.pushiOS_url)
    print(con_generic.pushiOSapi_key)
