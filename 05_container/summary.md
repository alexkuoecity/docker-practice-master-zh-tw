## 本章小結

本章介紹了 Docker 容器的啟動、停止、進入和刪除等核心操作。

| 操作 | 命令 | 說明 |
|------|------|------|
| 新建並執行 | `docker run` | 最常用的啟動方式 |
| 互動式啟動 | `docker run -it` | 用於除錯或臨時操作 |
| 後臺執行 | `docker run -d` | 用於服務類應用 |
| 啟動已停止的容器 | `docker start` | 重用已有容器 |
| 優雅停止 | `docker stop` | 先 SIGTERM，超時後 SIGKILL |
| 強制停止 | `docker kill` | 直接 SIGKILL |
| 重啟 | `docker restart` | 停止後立即啟動 |
| 停止全部 | `docker stop $(docker ps -q)` | 停止所有執行中容器 |
| 進入容器除錯 | `docker exec -it 容器名 bash` | 推薦方式 |
| 執行單條命令 | `docker exec 容器名 命令` | 不進入互動模式 |
| 檢視主程序輸出 | `docker attach 容器名` | 慎用，退出可能停止容器 |
| 刪除已停止容器 | `docker rm 容器名` | 需先停止 |
| 強制刪除執行中容器 | `docker rm -f 容器名` | 直接刪除 |
| 刪除容器及匿名卷 | `docker rm -v 容器名` | 同時清理匿名卷 |
| 清理所有已停止容器 | `docker container prune` | 批次清理 |

### 延伸閱讀

- [後臺執行](5.2_daemon.md)：理解 `-d` 引數和容器生命週期
- [進入容器](5.4_attach_exec.md)：操作執行中的容器
- [網路配置](../09_network/README.md)：理解埠對映的原理
- [資料管理](../08_data/README.md)：資料持久化方案
- [刪除映像檔](../04_image/4.3_rm.md)：清理映像檔
- [資料卷](../08_data/8.1_volume.md)：資料卷管理
---

> 📝 **發現錯誤或有改進建議？** 歡迎提交 [Issue](https://github.com/yeasy/docker_practice/issues) 或 [PR](https://github.com/yeasy/docker_practice/pulls)。
