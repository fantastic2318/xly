def show_message():
    if __name__ == "__main__":
        print(f"这是被自己调用的，__name__等于{__name__}")
    else:
        print(f"这是被别人调用的，__name__等于{__name__}")

show_message()