import os
extensions = [
    # 你原来所有扩展，比如 sphinx_rtd_theme
    "sphinx_password"
]
sphinx_password_global_password = os.getenv("DOC_PASSWORD")
sphinx_password_prompt = "请输入文档访问密码"
