# ShadowCrack

Crack linux shadow passwords using a wordlist.

## Config

### Shadow

``` sh
sudo cp /etc/shadow shadow.txt
sudo chmod +r shadow.txt
```

### Wordlist

``` sh
gunzip -k wordlist.txt.gz
```

## Usage

``` sh
python3 shadowcrack.py
```

## Help

``` sh
python3 shadowcrack.py -h
```

## Credits

https://github.com/TiagoANeves/TDTLinuxPWD
