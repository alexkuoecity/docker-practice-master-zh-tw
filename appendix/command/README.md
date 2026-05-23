# 附錄三：Docker 命令查詢

## 基本語法

Docker 命令有兩大類，用戶端命令和伺服器端命令。前者是主要的操作介面，後者用來啟動 Docker Daemon。

* 用戶端命令：基本命令格式為 `docker [OPTIONS] COMMAND [arg...]`；

* 伺服器端命令：基本命令格式為 `dockerd [OPTIONS]`。

可以透過 `man docker` 或 `docker help` 來檢視這些命令。

接下來的小節對這兩個命令進行介紹。
