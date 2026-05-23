## 本章小結

本章介紹了 Docker 映像檔的獲取、列出、刪除以及構建方式。

| 操作 | 命令 |
|------|------|
| 拉取映像檔 | `docker pull 映像檔名:標籤` |
| 拉取所有標籤 | `docker pull -a 映像檔名` |
| 指定平臺 | `docker pull --platform linux/amd64 映像檔名` |
| 用摘要拉取 | `docker pull 映像檔名@sha256:...` |
| 列出所有映像檔 | `docker images` |
| 按倉庫名過濾 | `docker images nginx` |
| 列出虛懸映像檔 | `docker images -f dangling=true` |
| 只輸出 ID | `docker images -q` |
| 顯示摘要 | `docker images --digests` |
| 自定義格式 | `docker images --format "..."` |
| 檢視空間佔用 | `docker system df` |
| 刪除指定映像檔 | `docker rmi 映像檔名:標籤` |
| 強制刪除 | `docker rmi -f 映像檔名` |
| 刪除虛懸映像檔 | `docker image prune` |
| 刪除未使用映像檔 | `docker image prune -a` |
| 批次刪除 | `docker rmi $(docker images -q -f ...)` |

### 延伸閱讀

- [獲取映像檔](4.1_pull.md)：從 Registry 拉取映像檔
- [列出映像檔](4.2_list.md)：檢視和過濾映像檔
- [刪除映像檔](4.3_rm.md)：清理本地映像檔
- [映像檔加速器](../03_install/3.9_mirror.md)：加速映像檔下載
- [Docker Hub](../06_repository/6.1_dockerhub.md)：官方映像檔倉庫
- [映像檔](../02_basic_concept/2.1_image.md)：理解映像檔概念
- [刪除容器](../05_container/5.6_rm.md)：清理容器
- [資料卷](../08_data/8.1_volume.md)：清理資料卷
---

> 📝 **發現錯誤或有改進建議？** 歡迎提交 [Issue](https://github.com/yeasy/docker_practice/issues) 或 [PR](https://github.com/yeasy/docker_practice/pulls)。
