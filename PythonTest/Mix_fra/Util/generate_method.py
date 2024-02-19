def generate_func(location_type, location_express,action,test_data):
    """
    组装函数表达式
    :param location_type:
    :param location_express:
    :param action:
    :param test_data:
    :return:
    """
    method_express = ""
    # location_type location_express 都为空 test_data 不为空 比如open_browser()、enter_url()
    if location_type is None and location_express is None and test_data is not None:
        #  dfdf
        if isinstance(test_data, int):
            method_express = action + "(" + str(test_data) + ")"
        else:
            method_express = action + "('" + test_data + "')"
    # location_type location_express test_data 都为空 比如max_windows()
    elif location_type is None and location_express is None and test_data is None:
        method_express = action + '()'

    # location_type location_express 都不为空 test_data 为空 比如switch_frame()
    elif location_type and location_express and test_data is None:
        method_express = action + "('" + location_type + "','" + location_express + "')"
    # location_type location_express test_data 都不为空  比如input_content()
    elif location_type and location_express and test_data:
        if isinstance(test_data, int):
            method_express = action + "('" + location_type + "','" + location_express + "'," + str(test_data) + ")"
        else:
            method_express = action + "('" + location_type + "','" + location_express + "','" + test_data + "')"
    print("------")
    return method_express
