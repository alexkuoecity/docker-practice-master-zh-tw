## 本章小結

本章詳細介紹了 Dockerfile 的所有核心指令，以下是各指令要點的速查表。

| 指令 | 作用 | 關鍵要點 |
|------|------|---------|
| **FROM** | 指定基礎映像檔 | 必須是第一條指令 |
| **RUN** | 在新層執行命令 | 合併命令、清理快取以減小體積 |
| **COPY** | 複製檔案 | 優先使用，支援 `--from` |
| **ADD** | 更高階的複製 | 自動解壓 tar，不推薦用於下載 |
| **CMD** | 容器啟動預設命令 | 可被 `docker run` 引數覆蓋 |
| **ENTRYPOINT** | 容器入口點 | 固定啟動命令，CMD 作為預設引數 |
| **ENV** | 設定環境變數 | 構建時 + 執行時均生效 |
| **ARG** | 構建引數 | 僅構建時生效，FROM 後需重新宣告 |
| **VOLUME** | 定義匿名卷 | VOLUME 之後的修改會丟失 |
| **EXPOSE** | 宣告埠 | 僅文件作用，不自動對映 |
| **WORKDIR** | 指定工作目錄 | 替代 `RUN cd`，目錄不存在會自動建立 |
| **USER** | 指定執行使用者 | 使用者必須已存在，推薦 gosu |
| **HEALTHCHECK** | 健康檢查 | 支援 starting/healthy/unhealthy 狀態 |
| **ONBUILD** | 延遲執行指令 | 只繼承一次，不可級聯 |
| **LABEL** | 新增後設資料 | 推薦 OCI 標準標籤，替代 MAINTAINER |
| **SHELL** | 更改預設 shell | 推薦 `["/bin/bash", "-o", "pipefail", "-c"]` |

### 生產映像檔快速檢查清單

在將映像檔推向生產之前，建議逐條過一遍以下清單：

- [ ] 基礎映像檔選擇了最小化版本（如 `alpine`、`distroless`）
- [ ] 使用了[多階段構建](7.17_multistage_builds.md)，最終映像檔不含編譯工具鏈
- [ ] 以非 root 使用者執行（`USER` 指令）
- [ ] `COPY` 優先於 `ADD`，且僅複製必要檔案
- [ ] `RUN` 指令合併了 `apt-get update && install && rm -rf /var/lib/apt/lists/*`
- [ ] 設定了 `HEALTHCHECK`
- [ ] 使用了 `.dockerignore` 排除 `.git`、`node_modules` 等無關檔案
- [ ] 映像檔標籤使用了具體版本號或 commit hash，而非 `latest`

> 更完整的編寫指南見[附錄：Dockerfile 最佳實踐](../appendix/best_practices.md)。

### 延伸閱讀

- [使用 Dockerfile 定製映像檔](../04_image/4.5_build.md)：Dockerfile 入門
- [多階段構建](7.17_multistage_builds.md)：最佳化映像檔大小
- [Dockerfile 最佳實踐](../appendix/best_practices.md)：編寫指南
- [安全](../18_security/README.md)：容器安全實踐
- [Compose 模板檔案](../11_compose/11.5_compose_file.md)：Compose 中的配置
---

> 📝 **發現錯誤或有改進建議？** 歡迎提交 [Issue](https://github.com/yeasy/docker_practice/issues) 或 [PR](https://github.com/yeasy/docker_practice/pulls)。
