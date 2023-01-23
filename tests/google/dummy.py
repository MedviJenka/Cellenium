import requests


CERTIFICATE = r"C:\Users\evgenyp\Desktop\Assets\star.ai-logix.net_2023_audc.pfx"
result = requests.get("https://nextgenkube.ai-logix.net", verify=CERTIFICATE).json()


if __name__ == '__main__':
    print(result)
