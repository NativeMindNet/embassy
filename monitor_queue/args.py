import argparse


#if __name__ == "__main__":
def get_args():
    parser = argparse.ArgumentParser(description="Embassy bot")
    parser.add_argument("url", help="URL")
    args = parser.parse_args()

    url=args.url
    return args