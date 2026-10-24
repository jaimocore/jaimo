# jaimo
Python library and toolkit for data science applications.

```
jaimo/
├── .github/
│   └── workflows/
│       └── publish.yml       # GitHub Actions 自动化发布到 PyPI 的工作流
├── src/
│   └── jaimo/                # 你的核心 Python 包代码目录
│       ├── __init__.py       # 包入口，通常在这里定义 __version__ 并导出常用接口
│       ├── core.py           # 核心逻辑/主类封装
│       ├── utils.py          # 工具函数（如数据清洗、常用数学统计工具等）
│       └── stats.py          # 面向数据科学的统计或分析模块（按需拆分）
├── tests/                    # 单元测试目录
│   ├── __init__.py
│   └── test_core.py          # 测试用例
├── .gitignore                # Git 忽略文件（已自动生成 Python 模板）
├── LICENSE                   # MIT 开源协议（已自动生成）
├── README.md                 # 项目详细说明文档（PyPI 的主页介绍会读取这里）
└── pyproject.toml            # 现代 Python 项目的元数据与打包配置文件
```

```bash
git clone https://github.com/jaimocore/jaimo.git
```

```bash
cd jaimo
```

```bash
pip install -e .
```