import os

files = {
    ".gitignore": "__pycache__/\n*.py[cod]\n.env\n.vscode/\n.idea/\n*.log\nvenv/\n",
    ".env.example": "OPENAI_API_KEY=sk-your-key\nGITHUB_TOKEN=ghp_your-token\nAGENT_MODEL=gpt-4o\n",
    "LICENSE": "MIT License\n\nCopyright (c) 2026 Enes Kok\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files.\n",
    "requirements.txt": "openai>=1.30.0\nlangchain>=0.2.0\nlanggraph>=0.1.0\nPyGithub>=2.3.0\nGitPython>=3.1.40\nfastapi>=0.111.0\nuvicorn>=0.30.0\npyyaml>=6.0\npython-dotenv>=1.0.0\npytest>=8.2.0\nrich>=13.7.0\nclick>=8.1.0\n",
    os.path.join("configs", "config.yaml"): "agent:\n  model: gpt-4o\n  temperature: 0.2\n  max_retries: 3\n\nwatcher:\n  mode: poll\n  poll_interval: 30\n\nvalidator:\n  test_command: pytest\n  timeout: 120\n\nmerger:\n  auto_merge: false\n  branch_prefix: fix/agent\n",
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {path}")

print("All files created!")