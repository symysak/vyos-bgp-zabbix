# VyOSのBGP Peersをzabbixで監視するやつ
IPv4/IPv6対応
## 注意点
zabbixユーザでvtyshが使えるように色々設定していますが、セキュリティ的に超微妙なため、使用する場合は自己責任でお願いいたします。
## 使い方
このリポジトリのディレクトリ構造は、vyosのディレクトリ構造を示している。
※zbx_export_templates.yamlとreadme.mdを除く
なので、それの通りにファイルを配置

templateをimport

完成！