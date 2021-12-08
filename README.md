[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/salasberryfin/pyndora">
    <img src="images/findora.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Pyndora</h3>

  <p align="center">
    Basic Python SDK for the Findora blockchain
    <br />
    <a href="https://github.com/salasberryfin/pyndora"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/salasberryfin/pyndora">View Demo</a>
    ·
    <a href="https://github.com/salasberryfin/pyndora/issues">Report Bug</a>
    ·
    <a href="https://github.com/salasberryfin/pyndora/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

**[This is still a WIP]** Basic Python SDK for the Findora blockchain
<br>
This is still so far from a completely usable SDK but I think it's a good starting 
point if the idea of a Python SDK for Findora is found to be useful.
<br>
Some of the complexities of the blockchain itself made it harder than expected to 
progress on developing the basic functionalities of the SDK and, the fact that 
some of the core crypto-related methods could not be reused from Python made it 
considerably tougher for the time I've been able to spent on it so far.
<br>
Still, I think it would be great to continue building on top of this project if the team 
finds it interesting.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

This project is entirely based on Python.

<!-- GETTING STARTED -->
## Getting Started

You can create your own virtual environment, install the required dependencies 
and test the implemented methods.

### Dependencies

* Clone the repository

```bash
git clone https://github.com/salasberryfin/pyndora
```

* Inside the project folder

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
```

* Install required dependencies

```bash
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

`examples.py` contains a few use cases that have been totally or partially 
implemented. Feel free to test them out/modify/break.
<br>
- First you can initialize your SDK session, as shown in [examples.py](examples.py) `create_session`
This SDK object holds the configuration for the current session, assuming 
sensible defaults for those parameters that are not passed.
```python
from pyndora.sdk import Sdk

env = {
    "host_url": "https://prod-forge.prod.findora.org",
    "cache_path": "./cache",
}

sdk = Sdk()
sdk.init(env)
```
You can later `reset` this session to the default values if needed.
```python
sdk.reset()
```
<br>
- Generate a new mnemonic and create wallet from it, as shown in  [examples.py](examples.py) 
`create_fra_keypair_from_mnemonic`.
```python
from pyndora.api import (
    keypair,
    transaction,
)

mnemonic = keypair.get_mnemonic(length=24, lang="english")
print(f"Mnemonic phrase: {mnemonic.ToStr()}")
wallet_info = keypair.restore_from_mnemonic(
    mnemonic=mnemonic.ToStr(),
    password=password,
)

print(f"""Wallet:\n
      address: {wallet_info.address}
      public_key: {wallet_info.public_key.decode("utf-8")}
      key_store: {wallet_info.key_store}
      key_pair: {wallet_info.key_pair}
      private_str: {wallet_info.private_str.decode("utf-8")}
      """)
```
*Encrypted store of `key_store` and `key_pair` not implemented.* -> Nice TODO 
if someone if willing to collaborate on understanding how it's done in Findora.
<br>
- Get FRA balance for given wallet - recovered from mnemonic, as shown in 
[examples.py](examples.py) `get_fra_balance`.
```python
from pyndora.api import (
    keypair,
    account,
)

mnemonic = "insert your own mnemonic string"

wallet_info = keypair.restore_from_mnemonic(
    mnemonic=mnemonic,
    password=password,
)

print(f"""Restored Wallet:\n
      address: {wallet_info.address}
      public_key: {wallet_info.public_key.decode("utf-8")}
      key_store: {wallet_info.key_store}
      key_pair: {wallet_info.key_pair}
      private_str: {wallet_info.private_str.decode("utf-8")}
      """)

balance = account.get_balance(wallet_info)

print(f"The balance for address {wallet_info.address} is: {balance}")
```
*Balance can only be retrieved for FRA assets.* How to retrieve asset code?
<br>
- Sending a given amount to a wallet address is not fully implemented but a snippet 
can be find in [examples.py](examples.py) `send_fra`.
```python
source_account_mnemonic = "insert your own mnemonic string"
# use your desired fra address
to_addr = "fra1c834rhrxsc659s44gjewu6uxyt0qfmy94a70ef5083yzxftxjtstqvdf3"

wallet_info = keypair.restore_from_mnemonic(
    mnemonic=source_account_mnemonic,
    password=password,
)

print(f"""Restored Wallet:\n
      address: {wallet_info.address}
      public_key: {wallet_info.public_key.decode("utf-8")}
      key_store: {wallet_info.key_store}
      key_pair: {wallet_info.key_pair}
      private_str: {wallet_info.private_str.decode("utf-8")}
      """)

    transaction.send_to_address(wallet_info, to_addr, "0.01")
```
*The transaction builder is not fully implemented and some assumptions had to 
be made for unknowm wasm methods.*


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - [@salasberryfin](https://twitter.com/salasberryfin)

Project Link: [https://github.com/salasberryfin/pyndora](https://github.com/salasberryfin/pyndora)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/salasberryfin/pyndora.svg?style=for-the-badge
[contributors-url]: https://github.com/salasberryfin/pyndora/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/salasberryfin/pyndora.svg?style=for-the-badge
[forks-url]: https://github.com/salasberryfin/pyndora/network/members
[stars-shield]: https://img.shields.io/github/stars/salasberryfin/pyndora.svg?style=for-the-badge
[stars-url]: https://github.com/salasberryfin/pyndora/stargazers
[issues-shield]: https://img.shields.io/github/issues/salasberryfin/pyndora.svg?style=for-the-badge
[issues-url]: https://github.com/salasberryfin/pyndora/issues
