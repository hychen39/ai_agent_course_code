# AI Agent 課程範例程式

本 repository 收錄 AI Agent 課程使用的 Jupyter Notebook（`.ipynb`）與 Python（`.py`）範例，供課堂示範、課後練習與程式實作使用。內容以 LangChain 與 LangGraph 為主，從呼叫語言模型開始，逐步介紹流程圖、工具呼叫與對話記憶。

## 環境準備

- Python 3.13 以上版本。
- 使用 `uv` 安裝專案套件與管理虛擬環境。
- 執行模型相關範例時，需要可使用對應模型的 OpenAI API key。

在 repository 根目錄執行：

```bash
uv sync --group dev
```

套件需求定義於 [`pyproject.toml`](pyproject.toml)，版本鎖定資訊記錄於 `uv.lock`。開發套件包含 Jupyter 與 ipykernel，供 notebook 使用。

### 設定 API key

在 repository 根目錄建立 `.env` 檔案，填入自己的金鑰：

```dotenv
OPENAI_API_KEY=你的_API_key
```

`first_openai_api.ipynb` 已包含 `load_dotenv()`。其他使用模型的 notebook 若尚未載入環境變數，請在建立模型之前執行：

```python
from dotenv import load_dotenv

load_dotenv()
```

請勿將 `.env` 或真實金鑰提交至 Git。模型呼叫可能產生 API 費用. 

## 執行範例

從 repository 根目錄啟動 Jupyter Notebook：

```bash
uv run jupyter notebook
```

開啟 `notebooks/` 下的檔案，依序由上而下執行儲存格。若使用 VS Code，請選擇此專案 `.venv` 對應的 Python 環境作為 notebook kernel。

目前的 [`main.py`](main.py) 是簡單的 Python 入口範例，可用下列指令執行：

```bash
uv run python main.py
```