[tool.black]
line-length = 88
target-version = ['py312']

[tool.isort]
profile = "black"

[tool.mypy]
python_version = 3.12
strict = true
ignore_missing_imports = true
