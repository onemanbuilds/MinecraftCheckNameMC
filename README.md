# MinecraftCheckNameMC
 Simple minecraft name checker suggested by one of the members on my discord server.
 
# Features
 - Useragent rotation.<br/>
 - Proxy / Proxyless mode.<br/>
 - Proxy support (https / socks4 / socks5).<br/>
 - Configurable in the configs.json.<br/>
 - You can generate usernames with the desired length.<br/>
 - You can generate uppercase names.<br/>
 - You can generate lowercase names.<br/>
 - You can generate uppercase & lowercase names.<br/>
 - You can generate just digits.<br/>
 - You can include digits in the usernames.<br/>
 - You can add a prefix to the usernames.<br/>
 - You can add a suffix to the usernames.<br/>
 - You can use multiple regexes to generate any username you want.<br/>
 - Customizable thread amount.<br/>
 - You can generate & check usernames, and you can check them from a txt.<br/>
 - Webhook support.<br/>
 - Webhook proxy support (https / socks4 / socks5).

# Installation
 Make sure you have python 3.8.7 or higher (or use the exe version at the releases tab).<br/>
 ```
 pip3 install -r requirements.txt
 ``` 

# Configs.json
 - use_proxy (0 - Proxyless | 1 - Proxy).<br/>
 - proxy_type (1 - HTTPS | 2 - SOCKS4 | 3 - SOCKS5).<br/>
 - threads (Higher means faster performance, but more chance for inaccurate results).<br/>
 - webhook_enable (0 - Disable webhook support | 1 - Enable webhook support).<br/>
 - webhook_url (Url for your webhook).<br/>
 - gen_type (1 - Generate with the configs.json settings | 2 - Generate with the regexes in the regex.txt).<br/>
 - check_method (1 - Generate & Check | 2 - Check from the usernames.txt).<br/>
 - username_case (1 - Lowercase | 2 - Uppercase | 3 - Uppercase & Lowercase | 4 - Only digits).<br/>
 - username_include_digits (0 - No digits in the usernames | 1 - Use digits in the usernames).<br/>
 - username_length (The length of the usernames).<br/>
 - username_prefix (Word before the usernames for example if the prefix is apple then the username will look like this applegeneratedusername).<br/>
 - username_suffix Word after the usernames for example if the suffix is apple then the username will look like this generatedusernameapple).<br/>

# Suggestion
![](https://i.ibb.co/g6tWk8p/suggestion.png)
  
# Legal
 - The software designed to perform website security testing.<br/>
 - The author is not responsible for any illegal use of these programs.<br/>
 - I am not accountable for anything you get into.<br/>
 - I am not accountable for any of your actions.<br/>
 - This is 100% educational, please do not misuse this tool.