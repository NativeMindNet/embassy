import argparse


#if __name__ == "__main__":
def get_args():
    parser = argparse.ArgumentParser(description="Embassy bot")
    parser.add_argument("url", help="URL")
    parser.add_argument("id", help="ID")
    args = parser.parse_args()

    url=args.url
    return args