## 本章小結

Docker Buildx 是 Docker 構建系統的重要進化，提供了高效、安全且支援多平臺的映像檔構建能力。

| 概念 | 要點 |
|------|------|
| **BuildKit** | 下一代構建引擎，Docker 23+ 預設啟用 |
| **快取掛載** | `RUN --mount=type=cache` 加速依賴安裝 |
| **Secret 掛載** | `RUN --mount=type=secret` 安全傳遞金鑰 |
| **buildx build** | 替代 `docker build`，支援更多構建功能 |
| **構建檢查** | `--check` 可在不執行構建的情況下檢查 Dockerfile 與構建引數 |
| **多架構構建** | `--platform` 引數一鍵構建多種架構映像檔 |
| **Manifest List** | 多架構映像檔的索引檔案 |
| **SBOM** | 透過 `--sbom=true` 生成軟體物料清單 |

### 延伸閱讀

- [Dockerfile 指令詳解](../07_dockerfile/README.md)：Dockerfile 編寫基礎
- [多階段構建](../07_dockerfile/7.17_multistage_builds.md)：最佳化映像檔體積
- [Dockerfile 最佳實踐](../appendix/best_practices.md)：編寫高效 Dockerfile
---

> 📝 **發現錯誤或有改進建議？** 歡迎提交 [Issue](https://github.com/yeasy/docker_practice/issues) 或 [PR](https://github.com/yeasy/docker_practice/pulls)。
