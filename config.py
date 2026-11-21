import os
extensions = [
    # 这里保留你原来所有扩展，例如 sphinx_rtd_theme
    "sphinx_password"
]
sphinx_password_global_password = os.getenv("DOC_PASSWORD")
sphinx_password_prompt = "请输入文档访问密码"
