# raspi_apps




```
$ sudo pip3 install -r requirements.txt  -t ./
$ sudo python3 my_shutdown.py
```



http://www.masatom.in/pukiwiki/Python/TIPS%BD%B8/



## サービス化したいばあい。

### Systemd のファイルコピー

```
$ sudo cp -pfr  ./raspi_shutdown.service /etc/systemd/system/
```

あとは自動起動設定

```
$ sudo systemctl enable raspi_shutdown
Created symlink /etc/systemd/system/multi-user.target.wants/raspi_shutdown.service → /etc/systemd/system/raspi_shutdown.service.

$ sudo systemctl list-unit-files --type service | grep raspi_shutdown
raspi_shutdown.service                            enabled
```

サービスの起動は下記コマンドで。

```
$ sudo systemctl start  raspi_shutdown

```

最後にログの参照方法


```
$ sudo journalctl  -f -u raspi_shutdown
```


ver.1.0.3