from app import app

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", dest = "port", default = "8080", help="Port Number")
    parser.add_argument("-e", "--envv", dest = "envirvar", default = "", help="Environment Variable")
    parser.add_argument("-v", "--value", dest = "value", default = "", help="Environment Variable Value")
    args = parser.parse_args()

    app.config[args.envirvar] = args.value

    app.run(port=args.port)
