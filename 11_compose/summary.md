## 本章小結

Docker Compose 是管理多容器應用的利器，透過 YAML 檔案宣告式地定義服務、網路和資料卷。

| 概念 | 要點 |
|------|------|
| **核心概念** | 服務 (service) 和專案 (project) |
| **配置檔案** | `compose.yaml` (推薦) 或 `docker-compose.yml` |
| **版本** | Compose V2 為 Go 編寫的 CLI 外掛，透過 `docker compose` 使用 |
| **啟動** | `docker compose up -d` 啟動所有服務 |
| **停止** | `docker compose down` 停止並移除容器 |
| **檢視狀態** | `docker compose ps` 檢視服務狀態 |
| **檢視日誌** | `docker compose logs` 檢視服務日誌 |
| **模板檔案** | 支援 `services`、`networks`、`volumes` 等頂級配置 |

### 延伸閱讀

- [Compose 模板檔案](11.5_compose_file.md)：詳細模板語法參考
- [Compose 命令說明](11.4_commands.md)：完整命令列表
- [網路配置](../09_network/README.md)：Docker 網路基礎
- [資料管理](../08_data/README.md)：資料卷管理
---

> 📝 **發現錯誤或有改進建議？** 歡迎提交 [Issue](https://github.com/yeasy/docker_practice/issues) 或 [PR](https://github.com/yeasy/docker_practice/pulls)。
