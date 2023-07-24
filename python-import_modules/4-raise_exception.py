def raise_exception():
    raise TypeError

if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as TE:
        print("Exception raised")
